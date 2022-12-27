from pyrogram import *
import requests
from config import neko







    
@neko.on_message(filters.text, group=100)
async def ai(Client:neko, message):
    chat_id = message.chat.id
    bot_id =int(1876246009) #your bot's user id
    msg=await neko.get_messages(chat_id, message.id)
    if msg.reply_to_message and msg.reply_to_message.from_user.id== bot_id:
        ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={message.text}").json()
        print(ai_gen)
        json = ai_gen["response"]
        await neko.send_message(chat_id=chat_id ,text=json , reply_to_message_id=message.id)

    

@neko.on_message(filters.command(commands=["AiChan69Bot"] , prefixes="@"))
async def username(Client:neko, message):
    chat_id = message.chat.id
    text = message.text
    fixed_text = text.replace("@Aichan69Bot ", "")
    ai_gen = requests.get(f"https://apikatsu.otakatsu.studio/api/chatbot/Iseria?message={fixed_text}").json()
    print(ai_gen)
    json = ai_gen["response"]
    await neko.send_message(chat_id=chat_id ,text=json , reply_to_message_id=message.id)