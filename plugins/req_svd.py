from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from bot import Bot
from config import FORCE_SUB_CHANNEL_2
from database.database import add_req_one

@Bot.on_chat_join_request(
    filters.chat(FORCE_SUB_CHANNEL_2)
)
async def join_reqs(client, join_req: ChatJoinRequest):
    user_id = join_req.from_user.id
    if join_req.chat.id == FORCE_SUB_CHANNEL_2:
        try:
            await add_req_one(user_id)
        except Exception as e:
            print(f"Error adding join request to req_one: {e}")
