import asyncio
import logging
import time

from pyrogram import Client, filters 
from pyrogram.errors import PeerIdInvalid, ChannelInvalid, FloodWait

from config import API_ID, API_HASH, BOT_TOKEN, LOG_ID, SUDOERS
from bot.utils.database import db

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

app = Client(
    "Approver",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
)

boot = time.time()
async def eval_bot():
    try:
        await app.start()
    except FloodWait as ex:
        LOGGER.warning(ex)
        await asyncio.sleep(ex.value)
    print(1)
    try:
        await app.send_message(chat_id=LOG_ID, text=f"<u><b>» {app.me.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{app.me.id}</code>\nɴᴀᴍᴇ : {app.me.first_name}\nᴜsᴇʀɴᴀᴍᴇ : @{app.me.username}")
        LOGGER.info(f"Bot Started As {app.me.first_name}")
    except Exception as e:
        print(e)
        exit()

asyncio.get_event_loop().run_until_complete(eval_bot())
