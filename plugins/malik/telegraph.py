import os
import shutil
from pyrogram import Client, filters
from telegraph import upload_file
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.malik.extra import get_file_id, f_onw_fliter, TMP_DOWNLOAD_DIRECTORY


@Client.on_message(
    filters.command(["telegraph", "tel"]) &
    f_onw_fliter
)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("Not supported!")
        return
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.message_id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply_text(message, text=document)
    else:
        await message.reply_photo(
            photo=f"https://telegra.ph{response[0]}",
            caption=f"<b>𝗅𝗂𝗇𝗄:-</b> <code>https://telegra.ph{response[0]}</code>\n\n ᴘᴏᴡᴇʀᴅ ʙʏ: @ᴍ_ʜᴏᴜsᴇ786",
            quote=True,
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("⚡️ Oᴘᴇɴ ʟɪɴᴋ ⚡️", url=f"https://telegra.ph{response[0]}"),
               InlineKeyboardButton("♻️ Sʜᴇʀᴇ ʟɪɴᴋ ♻️", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
               ],[
               InlineKeyboardButton("💢 Cʟᴏᴠᴇ 💢", callback_data="close_data")
               ]]
            ),
            parse_mode='html'
)
    finally:
        os.remove(download_location)
