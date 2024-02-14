from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import filters

from src import app

@app.on_message(filters.command("start"))
async def strt(app, message: Message):
  await message.reply_photo(photo="https://graph.org/file/6be5258519aab54f2c2e8.jpg", caption=f"{app.me.mention} ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ.", 
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.me.username}?startgroup=true")]]))
