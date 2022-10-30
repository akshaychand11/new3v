#sahid malik
from info import MAINTENANCE_MODE, AUTH_USERS
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton





@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_filter(client, message):
    if MAINTENANCE_MODE:
        if AUTH_USERS and message.from_user and message.from_user.id in AUTH_USERS:
            k = await manual_filters(client, message)
            if k == False:
                await auto_filter(client, message)
        else:
            btn = [
        [
            InlineKeyboardButton('⚡️ ℂ𝕀ℕ𝔼𝕄𝔸 ℍ𝕌𝔹 ⚡️', url=f'https://t.me/cinemaforyou07')
        ]
        ]
        await message.reply_text(f"🔰𝗡𝗢𝗧𝗜𝗖𝗘🔰\n\nService is 𝕔𝕝𝕠𝕤𝕖𝕕 for 𝟮 𝘄𝗲𝗲𝗸𝘀.\nwill start again by <u>next month.</u>.\n\n𝖡𝗒 𝗍𝗁𝗂𝗌 𝗍𝗂𝗆𝖾, 𝖬𝖺𝗄𝖾 𝗌𝗎𝗋𝖾 <b>you have 𝗌𝗎𝖻𝗌𝖼𝗋𝗂𝖻𝖾𝖽 CINEMA HUB group👇🏻</b>", reply_markup=InlineKeyboardMarkup(btn))    
    else:
        k = await manual_filters(client, message)
        if k == False:
            await auto_filter(client, message)

