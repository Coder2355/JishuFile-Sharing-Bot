

from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
import sys
from datetime import datetime
from config import API_HASH, API_ID, LOGGER, BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT, FORCE_SUB_CHANNEL, ADMINS
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

# Force subscribe channels as a set to allow dynamic modification
force_sub_channels = set(FORCE_SUB_CHANNEL) if isinstance(FORCE_SUB_CHANNEL, list) else {FORCE_SUB_CHANNEL}

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.invitelink = {}

        for channel in force_sub_channels:
            try:
                link = (await self.get_chat(channel)).invite_link
                if not link:
                    await self.export_chat_invite_link(channel)
                    link = (await self.get_chat(channel)).invite_link
                self.invitelink[channel] = link
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(f"Failed to export invite link for channel ID {channel}")
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Hey 🖐")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning("Please check the CHANNEL_ID value.")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot Running...!")
        self.username = usr_bot_me.username

        # Start web server
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped...")


bot = Bot()


@bot.on_message(filters.command("add_channel") & filters.user("ADMINS"))
async def add_channel(bot: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /add_channel <channel_id>")
        return

    channel_id = message.command[1]
    try:
        await bot.get_chat(channel_id)
        force_sub_channels.add(channel_id)
        await message.reply_text(f"Channel {channel_id} added to force subscribe list.")
    except Exception as e:
        await message.reply_text(f"Failed to add channel: {e}")


@bot.on_message(filters.command("rem_channel") & filters.user("ADMINS"))
async def remove_channel(bot: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /rem_channel <channel_id>")
        return

    channel_id = message.command[1]
    if channel_id in force_sub_channels:
        force_sub_channels.remove(channel_id)
        await message.reply_text(f"Channel {channel_id} removed from force subscribe list.")
    else:
        await message.reply_text(f"Channel {channel_id} is not in the force subscribe list.")
    

# Only start the bot if this file is run directly
if __name__ == "__main__":
    bot.run()
