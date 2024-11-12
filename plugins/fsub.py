from pyrogram import Client, filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNEL
from bot import Bot

@Bot.on_message(filters.command("add_channel") & filters.user(ADMINS))  # Ensure only admins can run this command
async def add_channel(client: Client, message: Message):
    if FORCE_SUB_CHANNEL is not None:
        await message.reply_text("A force subscribe channel is already set.")
        return

    # Extract channel ID or username from the command
    if len(message.command) < 2:
        await message.reply_text("Please provide a valid channel ID or username.")
        return
    
    channel_id = message.command[1]
    
    try:
        # Check if the bot is an admin in the specified channel
        chat_member = await client.get_chat_member(channel_id, client.me.id)
        if chat_member.status not in ["administrator", "creator"]:
            await message.reply_text("Please make sure the bot is an admin in the force subscribe channel.")
            return
        
        # Set force_subscribe to the provided channel ID if bot is admin
        FORCE_SUB_CHANNEL = channel_id
        await message.reply_text(f"Force subscribe channel has been set to: {channel_id}")
    
    except Exception as e:
        await message.reply_text(f"Error: {e}")

@Bot.on_message(filters.command("Rem_channel") & filters.user(ADMINS))  # Only admins can run this command
async def remove_channel(client: Client, message: Message):
    if FORCE_SUB_CHANNEL is None:
        await message.reply_text("No force subscribe channel is set.")
    else:
        # Reset force_subscribe to None
        FORCE_SUB_CHANNEL = None
        await message.reply_text("Force subscribe channel has been removed.")
