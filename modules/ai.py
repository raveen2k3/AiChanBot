from pyrogram import filters, Client 
from pyrogram.types import Message
import requests
from config import neko, BOT_ID


@neko.on_message(filters.text, group=100)
async def ai(_, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user.id == BOT_ID:
        ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={message.text}", timeout=5).json()["response"]
        print(ai_gen)
        await neko.send_message(chat_id=message.chat.id ,text=ai_gen , reply_to_message_id=message.id)

    

@neko.on_message(filters.command(commands=["AiChan69Bot"] , prefixes="@"))
async def username(_, message: Message):
    fixed_text = message.text.replace("@Aichan69Bot ", "")
    ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={fixed_text}", timeout=5).json()["response"]
    print(ai_gen)
    await neko.send_message(chat_id=message.chat.id ,text=ai_gen, reply_to_message_id=message.id)
