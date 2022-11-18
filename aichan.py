from pyrogram import *
import requests
from pyrogram.types import *
from config import api_hash , api_id , bot_token , luna_key


neko = Client(name="aichan" , api_hash= api_hash , api_id=api_id , bot_token=bot_token)

@neko.on_message(filters.command("start"))
async def start(client:neko,message):
    keyboard = [
        [
            InlineKeyboardButton("JOIN",
                                          url="https://t.me/ProjectBaka"),
            InlineKeyboardButton("Support",
                                          url="https://t.me/BakaSupport"),
            InlineKeyboardButton("SHARE",url="https://t.me/share/url?url=https://t.me/AiChanSusBot")
        ],
    ]
    await message.reply_text(text =
                              "<b>Hey! Im AI-CHAN.</b>"
                              "\nI can help you explore many stuffs ,ask me anything."
                              "\n\n<b>About Me :</b>"
                              "\n\n  - <b>Name</b>        : <a href=\"https://t.me/its_raveen/\">Ai Chan</a>"
                              "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/its_raveen/\">Raveen</a>"
                              "\n\n  - <b>Language</b>  : <a href=\"https://www.python.org/\">Python 3</a>"
                              "\n\n  - <b>Api Owner</b> : <a href=\"https://t.me/TheAwakenedStb\">STB</a>"
                              "\n\n  - <b>Api Source</b>      : <a href=\"https://t.me/LunaNotice/101\">SOURCE</a>"
                              "\n\n  - <b>Library</b>       : <a href=\"https://docs.pyrogram.org/\">PYROGRAM</a>"
                              "\n\n  - <b>Source Code</b>  : <a href=\"https://github.com/raveen2k3/AiChanBot\">Source Code</a>",    
        disable_web_page_preview = True ,
        reply_markup = InlineKeyboardMarkup(keyboard)
     )

    
@neko.on_message(filters.text)
async def ai(Client:neko, message):
    chat_id = message.chat.id
    text = message.text
    ai_gen = requests.get(f"http://Iseria.up.railway.app/api={luna_key}/prompt={text}").json()
    await neko.send_message(chat_id=chat_id ,text=ai_gen)
    






neko.run()