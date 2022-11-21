import os
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE
from utils import extract_user, get_file_id, last_online, temp
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"<b>➲ First Name:</b> {first}\n<b>➲ Last Name:</b> {last}\n<b>➲ Username:</b> {username}\n<b>➲ Telegram ID:</b> <code>{user_id}</code>\n<b>➲ Data Centre:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        _id = ""
        _id += (
            "<b>➲ Chat ID</b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "<b>➲ Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )

@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>➲First Name:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>➲Last Name:</b> {last_name}\n"
    message_out_str += f"<b>➲Telegram ID:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str += f"<b>➲Data Centre:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>➲User Name:</b> @{username}\n"
    message_out_str += f"<b>➲User 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type in ((enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL)):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = (
                chat_member_p.joined_date or datetime.now()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>➲Joined this Chat on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
    await status_message.delete()


# help commands 

@Client.on_message(filters.command("help"))
async def help(client, message):
        buttons = [[
            InlineKeyboardButton('ᴀᴜᴛᴏ ғɪʟᴛᴇʀ', callback_data='autofilter'),
            InlineKeyboardButton('ᴄᴏɴɴᴇᴄᴛɪᴏɴs', callback_data='coct')
        ], [
            InlineKeyboardButton('ᴇxᴛʀᴀ ᴍᴏᴅᴇs', callback_data='GHHM'),
            InlineKeyboardButton('ʜᴏᴍᴇ ', callback_data='start'),
            InlineKeyboardButton('sᴏɴɢs', callback_data='songs')
        ], [
            InlineKeyboardButton('sᴛᴀᴛs', callback_data='stats'),
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜ', callback_data='tel'),
            InlineKeyboardButton('ᴏᴡɴᴇʀ', callback_data='my_detals')
        ], [
            InlineKeyboardButton('ʏᴛ-ᴛʜᴜᴍʙ', callback_data='ytthumb'),
            InlineKeyboardButton('ᴠɪᴅᴇᴏ', callback_data='video'),
            InlineKeyboardButton('ғɪʟᴇ-sᴛᴏʀᴇ', callback_data='malikk')
        ], [
            InlineKeyboardButton('ᴍᴜᴛᴇ', callback_data='mute'),
            InlineKeyboardButton('ʀᴇᴘᴏʀᴛ', callback_data='report'),
            InlineKeyboardButton('ᴘᴜʀɢᴇ', callback_data='purges'),
        ], [
            InlineKeyboardButton('ғᴏɴᴛs', callback_data='fonts'),
            InlineKeyboardButton('sᴛɪᴄᴋᴇʀ', callback_data='stkr'),
            InlineKeyboardButton('ᴡʀɪᴛᴇ ᴛᴇxᴛ', callback_data='write'),
        ], [
            InlineKeyboardButton('🚶‍♀ 𝐁𝐀𝐂𝐊 🚶‍♀', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=script.HELP_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
     
# about commands 
@Client.on_message(filters.command("about"))
async def about(client, message):
        buttons = [[
            InlineKeyboardButton('🌴 ʙᴏᴛs ᴄʜᴀɴɴᴇʟ 🌴', url='https://t.me/malik_bots'),
            InlineKeyboardButton('♥️ sᴏᴜʀᴄᴇ', callback_data='source')
        ], [
            InlineKeyboardButton('ʜᴏᴍᴇ ', callback_data='start'),
            InlineKeyboardButton('ᴄʟᴏᴄᴇ', callback_data='close_data')
        ], [
            InlineKeyboardButton('📞 ᴏᴡɴᴇʀ', url='https://t.me/sahid_malik'),
            InlineKeyboardButton('❤️ ᴅᴏɴᴀᴛɪᴏɴ ❤️', callback_data='malik')
        ], [
            InlineKeyboardButton('🚶‍♀ 𝐛𝐚𝐜𝐤 🚶‍♀', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
  
