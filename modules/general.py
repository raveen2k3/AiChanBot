#genral handlers
from pyrogram import filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .broadcast import addusertoDb
from config import *
@neko.on_message(filters.command(["start"] ))
async def start(client, message):
    try:
        await message.reply_text(
        text=f"**Hello {message.from_user.first_name} 👋 !"
             "\n\nFeeling Tired of Useless Ai Bots? , AiChan is here to rescue. "
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
    ),addusertoDb(message)

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
        ),addusertoDb(message)

        
@neko.on_message(filters.command("about"))
async def about(client:neko,message):
    keyboard = [
        [
            InlineKeyboardButton("Updates",
                                          url="https://t.me/BakaForum"),
            InlineKeyboardButton("Support",
                                          url="https://t.me/BakaForum"),
            InlineKeyboardButton("SHARE",url="https://t.me/share/url?url=https://t.me/AiChan69Bot")
        ],
    ]
    await message.reply_text(text =
                              "<b>Hey! Im AI-CHAN.</b>"
                              "\nI can help you explore many stuffs ,ask me anything."
                              "\n\n<b>About Me :</b>"
                              "\n\n  - <b>Name</b>        : <a href=\"https://t.me/its_raveen/\">Ai Chan</a>"
                              "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/its_raveen/\">Raveen</a>"
                              "\n\n  - <b>Language</b>  : <a href=\"https://www.python.org/\">Python 3</a>"
                              "\n\n  - <b>Library</b>       : <a href=\"https://docs.pyrogram.org/\">PYROGRAM</a>"
                              "\n\n  - <b>Source Code</b>  : <a href=\"https://github.com/raveen2k3/AiChanBot\">Source Code</a>",    
        disable_web_page_preview = True ,
        reply_markup = InlineKeyboardMarkup(keyboard)
     )
    
donate_sus = "https://graph.org/file/1d609c5089ef2c1a7e6be.mp4"
@neko.on_message(filters.command(["donate"]))
async def donate(client, message):
    chat_id =message.chat.id
    sponsor_msg = """First of All Im Thanking you for using \n\n/donate option
    \n\n Due To The Poor Server We Have In Our Hand We cant Provide You Better Service
    \n\n It would be be a great help if You Can Help Us To Improve Our Server
    \n\n you can use sponsor button by clicking below
    \n\n feel free to msg in group for alternative Payment Method :-)
    \n\n Anyways this Service will always be free And we Wont force You to pay us"""
    
    await neko.send_animation(chat_id, animation=donate_sus ,caption=sponsor_msg , reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Support", url="https://telegram.me/BakaForum"),
                    InlineKeyboardButton(text="Donate" , url="https://github.com/sponsors/raveen2k3") ,
                    
                    


                ]
            ]
        )
    )  
    
    

    
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
    await neko.send_message(chat_id , text ,reply_to_message_id=message.id)
    
    
@neko.on_callback_query()
async def cb_handler(neko, query):
    if query.data == "About":
        
        await query.answer()
        
        keyboard = [
            [
                InlineKeyboardButton("Updates",
                                            url="https://t.me/BakaForum"),
                InlineKeyboardButton("Support",
                                            url="https://t.me/BakaForum"),
                InlineKeyboardButton("Share",url="https://t.me/share/url?url=https://t.me/AiChan69Bot")
            ],
                    ]
        await query.message.edit_text(text =
                                "<b>Hey! Im AI-CHAN.</b>"
                                "\nI can help you explore many stuffs ,ask me anything."
                                "\n\n<b>About Me :</b>"
                                "\n\n  - <b>Name</b>         : <a href=\"https://t.me/its_raveen/\">Ai Chan</a>"
                                "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/BakaForum/\">Raveen</a>"
                                "\n\n  - <b>Language</b>     : <a href=\"https://www.python.org/\">Python 3</a>"
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
                                            url="https://t.me/BakaForum"),
                InlineKeyboardButton("Support",
                                            url="https://t.me/BakaForum"),
                InlineKeyboardButton("Share",url="https://t.me/share/url?url=https://t.me/AiChan69Bot")
            ],
                    ]
        help_text ="""Hey Mate first checkout my /guidelines
        \n\n just send me your query i may able to answer it!
        \n\n Join Our Support group, for feature request or bug fixes
        """
        
        
        await query.message.edit_text(text=help_text, reply_markup = InlineKeyboardMarkup(keyboard))