#sahid malik
from info import MAINTENANCE_MODE, AUTH_USERS
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton





@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_filter(client, message):
    if MAINTENANCE_MODE:
        if AUTH_USERS and message.from_user and message.from_user.id in AUTH_USERS:
            k = await manual_filters(client, message)
            if k == False:
                await auto_filter(client, message)
        else:
            await message.reply_text(f"🔰𝗡𝗢𝗧𝗜𝗖𝗘🔰\n\nService is 𝕔𝕝𝕠𝕤𝕖𝕕 for 𝟮 𝘄𝗲𝗲𝗸𝘀.\nwill start again by <u>next month.</u>.\n\n𝖡𝗒 𝗍𝗁𝗂𝗌 𝗍𝗂𝗆𝖾, 𝖬𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 <b>you have 𝗌𝗎𝖻𝗌𝖼𝗋𝗂𝖻𝖾𝖽 CINEMA HUB group👇🏻</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚶 Back to Group 🚶",url="https://t.me/+FAgX05kGByNkZjJl"),]]),parse_mode=enums.ParseMode.HTML)#"You are now verified for next 24 hours. Continue asking movies")      

    else:
        k = await manual_filters(client, message)
        if k == False:
            await auto_filter(client, message)

