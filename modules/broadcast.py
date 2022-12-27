from pymongo import MongoClient
from config import DB_URL, DB_NAME, OWNERID, neko
from pyrogram import filters
from pyrogram.types import Message

DB = MongoClient(DB_URL)[DB_NAME]["users"]

def addusertoDb(message: Message):
    if DB.find_one({'userid': message.from_user.id}):
        return
    DB.insert_one({
        'userid': message.from_user.id,
        'chattype': message.chat.type,
        'username': message.from_user.username,
        'firstname': message.from_user.first_name,
        'lastname': message.from_user.last_name,
    })
    

    
@neko.on_message(filters.command(["brodcast"]) & filters.user(OWNERID))
async def brodcast(_ , message: Message):
    if not message.reply_to_message_id:
        return 
    failed = []
    for receiver in [c["userid"] for c in DB.find()]:
        try:
            await neko.forward_messages(chat_id=receiver, from_chat_id=message.chat.id , message_ids=message.reply_to_message.id)
        except:
            failed.append(receiver)
            continue
    await neko.send_message(OWNERID, f"brodcast failed to {failed}")