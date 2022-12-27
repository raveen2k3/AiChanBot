from pyrogram import Client
from os import getenv
from dotenv import load_dotenv


load_dotenv()
API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID"))
TOKEN = getenv("TOKEN")
OWNERID = int(getenv("OWNERID"))  # your userid
BOT_ID = int(getenv("BOT_ID"))
DB_URL = getenv("DB_URL")
DB_NAME = getenv("DB_NAME")

neko = Client(name="aichan", api_hash=API_HASH, api_id=API_ID,
              bot_token=TOKEN, plugins={"root": "modules"})
