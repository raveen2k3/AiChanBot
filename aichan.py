from pyrogram import *
import requests
from pyrogram.types import *
from config import api_hash , api_id , bot_token , luna_key


neko = Client(name="aichan" , api_hash= api_hash , api_id=api_id , bot_token=bot_token)

@neko.on_message(filters.command(["start"] ))
async def start(client, message):
    try:
        await message.reply_text(
        text=f"**Hello {message.chat.first_name} 👋 !"
             "\n\nFeeling Tired of Using Bad Ai Bots? , AiChan is here rescue. "
             "\n\nCheck About to know the use of me**",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("About", callback_data="About"),
                    InlineKeyboardButton("Help" , callback_data="Help")
                ]
            ]
        ),
        reply_to_message_id=message.id
    )
    except:
        await message.reply_text(
            text=f"**Hi 👋 !"
                 "\n\nFeeling Tired of Using Bad Ai Bots? , AiChan is here rescue."
                 "\n\nCheck Help to find out more on how to use me.**",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("About", callback_data="About"),
                        InlineKeyboardButton("Help" , callback_data="Help")
                    ]
                ]
            ),
            reply_to_message_id=message.id
        )


@neko.on_message(filters.command("about"))
async def about(client:neko,message):
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

    
@neko.on_message(filters.text, group=100)
async def ai(Client:neko, message):
    chat_id = message.chat.id
    bot_id =int(1876246009)
    msg=await neko.get_messages(chat_id, message.id)
    if msg.reply_to_message and msg.reply_to_message.from_user.id== bot_id:
        ai_gen = requests.get(f"http://Iseria.up.railway.app/api={luna_key}/prompt={msg}").json()
        if "Luna" in ai_gen:
            final_text1 = ai_gen.replace("Luna","Aichan")
            await neko.send_message(chat_id=chat_id ,text=final_text1 , reply_to_message_id=message.id)

        elif "STB" in ai_gen:
            final_text2= ai_gen.replace("STB","@ProjectBaka")
            await neko.send_message(chat_id=chat_id ,text=final_text2 , reply_to_message_id=message.id)

        elif "/guidelines" in message.text:
            print("uff exception")
        elif "/start" in message.text:
            print("kek")
        elif "/about" in message.text:
            print("exception")
        else:
            final_text=ai_gen
            await neko.send_message(chat_id=chat_id ,text=final_text , reply_to_message_id=message.id)
            
#rename the command handler
@neko.on_message(filters.command(commands=["AiChan69Bot"] , prefixes="@"))
async def username(Client:neko, message):
    chat_id = message.chat.id
    text = message.text
    fixed_text = text.replace("@Aichan69Bot ", "")
    ai_gen = requests.get(f"http://Iseria.up.railway.app/api={luna_key}/prompt={fixed_text}").json()
    if "Luna" in ai_gen:
        final_text1 = ai_gen.replace("Luna","Aichan")
        await neko.send_message(chat_id=chat_id ,text=final_text1 , reply_to_message_id=message.id)

    elif "STB" in ai_gen:
        final_text2= ai_gen.replace("STB","@ProjectBaka")
        await neko.send_message(chat_id=chat_id ,text=final_text2 , reply_to_message_id=message.id)
    elif "/guidelines" in text:
        print("uff exception")
    elif "/start" in text:
        print("kek")
    else:
        final_text=ai_gen
        await neko.send_message(chat_id=chat_id ,text=final_text , reply_to_message_id=message.id)
    
    
        
    
    
    

    
@neko.on_message(filters.command("guidelines"))
async def guidelines(client:neko,message):
    chat_id = message.chat.id
    text = """There are some general guidelines that everyone should follow when chatting with AiChan!.
    \n\nit is important to be respectful and courteous. 
    \n\nDo not use profanity or obscene language,
    \n\ndo not spam the chatbot with multiple messages, do not send duplicate messages.
    \n\nAdditionally, it is important to remember that even though AiChan is advanced, 
    \n\nit is not perfect and may not always understand what you are saying. 
    \n\nIf you are having difficulty communicating with it,
    \n\nit is best to try rephrasing your questions or statements."""
    await neko.send_message(chat_id , text)
    
    



@neko.on_callback_query()
async def cb_handler(neko, query):
    if query.data == "About":
        
        await query.answer()
        
        keyboard = [
            [
                InlineKeyboardButton("Announcement",
                                            url="https://t.me/ProjectBaka"),
                InlineKeyboardButton("Support",
                                            url="https://t.me/BakaSupport"),
                InlineKeyboardButton("Share",url="https://t.me/share/url?url=https://t.me/AiChan69Bot")
            ],
                    ]
        await query.message.edit_text(text =
                                "<b>Hey! Im AI-CHAN.</b>"
                                "\nI can help you explore many stuffs ,ask me anything."
                                "\n\n<b>About Me :</b>"
                                "\n\n  - <b>Name</b>         : <a href=\"https://t.me/its_raveen/\">Ai Chan</a>"
                                "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/its_raveen/\">Raveen</a>"
                                "\n\n  - <b>Language</b>     : <a href=\"https://www.python.org/\">Python 3</a>"
                                "\n\n  - <b>Api Owner</b>    : <a href=\"https://t.me/TheAwakenedStb\">STB</a>"
                                "\n\n  - <b>Api Source</b>   : <a href=\"https://t.me/LunaNotice/101\">SOURCE</a>"
                                "\n\n  - <b>Library</b>      : <a href=\"https://docs.pyrogram.org/\">PYROGRAM</a>"
                                "\n\n  - <b>Source Code</b>  : <a href=\"https://github.com/raveen2k3/AiChanBot\">Source Code</a>",    
            disable_web_page_preview = True ,
            reply_markup = InlineKeyboardMarkup(keyboard)
            
        )
        
    elif query.data == "Help":
        await query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Announcements",
                                            url="https://t.me/ProjectBaka"),
                InlineKeyboardButton("Support",
                                            url="https://t.me/BakaSupport"),
                InlineKeyboardButton("Share",url="https://t.me/share/url?url=https://t.me/AiChan69Bot")
            ],
                    ]
        help_text ="""Hey Mate first checkout my /guidelines
        \n\n just send me your query i may able to answer it!
        \n\n Join Our Support group, for feature request or bug fixes
        """
        
        
        await query.message.edit_text(text=help_text, reply_markup = InlineKeyboardMarkup(keyboard))
    






neko.run()
