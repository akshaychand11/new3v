#sahid malik
from plugins.malik.extra import G_FILTER
from info import PM_MAINTENANCE_MODE, PM_MAINTENANCE_MODE2, LOG_CHANNEL
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_text(client, message):
    if PM_MAINTENANCE_MODE:
        content = message.text
        user = message.from_user.mention
        if content.startswith("/") return #
        await message.reply_text(text=(G_FILTER.format(user)), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡️ Backup Channel ⚡️",url="https://t.me/+FAgX05kGByNkZjJl"),]]),parse_mode=enums.ParseMode.HTML)  
        return 




@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_text(client, message):
        contents = msg.text
        user = msg.from_user.first_name
        if content.startswith("/") or contents.startswith("#"): return #
        await msg.reply_text("<b>Your message has been sent to my moderators !</b>")
        await bot.send_msg(
            chat_id=LOG_CHANNEL,
            text=f"<b>#PM_MSG\n\nName : {user}\n\nID : {user_id}\n\nMessage : {contents}</b>"
        )
