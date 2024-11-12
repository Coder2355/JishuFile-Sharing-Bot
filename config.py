import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7444872585:AAHYzPX_gygFh9xYvu0-k7YOUg7BSG_hzHg")
API_ID = int(os.environ.get("API_ID", "21740783"))
API_HASH = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")


OWNER_ID = int(os.environ.get("OWNER_ID", "6299192020"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "Speedwolf1")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002134913785"))

FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", None)


START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/feb6dd0a1cb8576943c0f.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://vault.pictures/p/82768980717549f78d41bd8a07898cac")

FILE_AUTO_DELETE = os.getenv("FILE_AUTO_DELETE", None) # auto delete in seconds


PORT = os.environ.get("PORT", "8020")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6299192020]
    for x in (os.environ.get("ADMINS", "6299192020").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Sry You can't Able to Message me !\n\n» My Owner 👉 @Anime_warrior_tamil"

START_MSG = os.environ.get("START_MESSAGE", "<b>Hi {first} Friend I am a Advance File Store bot 😈 \n\n I was created by 👉@Anime_warrior_tamil </b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} Neenga innum 03 channel la join pannala..\n\n 𝐒𝐨 join pannitu indha button click pannunga “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")




ADMINS.append(OWNER_ID)
ADMINS.append(6299192020)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href='https://t.me/Occoccicfx_bot'>[AW] File store bot 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Anime_Warrior_Tamil'>AWT BOTS</a>
<b>🛡️ :</b> <a href='https://t.me/+NITVxLchQhYzNGZl'>AWT Developer</a>
    
<b>😈 Bot Made By :</b> @AWT_Bot_Developer"""
