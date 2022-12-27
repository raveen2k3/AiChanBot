import pymongo
from config import *
from pyrogram import filters



def addusertoDb(message):
    my_client = pymongo.MongoClient(DB_URL)
    
    Database = my_client[DB_NAME]
    userid=message.from_user.id
    chat_type = message.chat.type
    collection = Database["users"]
    result = collection.find_one({'userid': userid})

    if result:
        if result.get('userid'): return
        
    username = message.from_user.username
    firstname = message.from_user.first_name
    lastname = message.from_user.last_name
    
    user = {}
    user['userid'] = userid
    user['chattype'] = str(chat_type)
    user['username'] = username
    user['firstname'] = firstname
    user['lastname'] = lastname

    collection.insert_one(user)
    
    
@neko.on_message(filters.command(["brodcast"]))
async def brodcast (client , message):
    user_id = message.from_user.id
    if user_id == OwnerId:
        o = []

        try:
                
            my_client = pymongo.MongoClient(DB_URL)
        
            Database = my_client[DB_NAME]
            userid=message.from_user.id
            collection = Database["users"]
            receivers = [c["userid"] for c in collection.find()]
            for receiver in receivers:
                try:
                    message_to_send = message.reply_to_message.id
                    print(receiver)
                    
                    await neko.forward_messages(chat_id=receiver, from_chat_id=message.chat.id , message_ids=message_to_send)
                except:
                    o.append(receiver)
                    await neko.send_message(chat_id=OwnerId, text="brodcast failed to " + str(o))
                    continue
                
                
        except Exception as e:
            
            error_msg = str(e)
            await neko.send_message(chat_id=OwnerId, text=error_msg)