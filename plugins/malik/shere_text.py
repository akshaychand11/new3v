from os import environ
import asyncio
from urllib.parse import *
from pyrogram import Client, filters, enums 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import *
from pyrogram import *
from utils import temp 

@Client.on_message(filters.command(["share"]))
async def sharelink(client, message): 
    text = message.text.split(" ",1)[1]
    await message.reply_photo(
        photo=(MALIK),
        caption=(MALIKK.format(message.from_user.mention, temp.U_NAME, temp.B_NAME, message.chat.title)),
        reply_markup=InlineKeyboardMarkup(
                               [[
                                 InlineKeyboardButton('💢 Share Link 💢', url=f"https://t.me/share/url?url={quote(text)}"),
                                                                         
                               ]]
        ),
        parse_mode=enums.ParseMode.HTML
)
    
MALIKK = """Successfully Create Share link 💘\n\n🥸Requested by: {}.\n🔹Creator by: <a href=https://t.me/{}>{}</a>\n💻 Group {}."""

MALIK = environ.get("MALIK", "https://telegra.ph/file/51cf57fe4c431a4af013b.jpg")
