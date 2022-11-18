#sahid malik
from plugins.malik.extra import G_FILTER
from info import PM_MAINTENANCE_MODE, LOG_CHANNEL, ADMINS, REQ_GRP
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




@Client.on_message(filters.command("send") & filters.chat(ADMINS))
async def send_msg(bot, message):
    if message.reply_to_message:
        target_id = message.text
        command = ["/send "]
        for cmd in command:
            if cmd in target_id:
                target_id = target_id.replace(cmd, "")
        success = False
        try:
            user = await bot.get_users(int(target_id))
            await message.reply_to_message.copy(int(user.id))
            success = True
        except Exception as e:
            await message.reply_text(f"<b>Must give a valid chat id ! \nError: {e}</b>")
        if success:
            await message.reply_text(f"<b>Your message has been successfully send to {user.mention}.</b>")
        else:
            await message.reply_text("<b>An error occurred !</b>")
    else:
        await message.reply_text("<b>Use this command as a reply to any message using the target chat id. For eg: /send userid</b>")




@Client.on_message(filters.text & filters.private & filters.incoming)
async def g_text(bot, message):
        content = message.text
        user = message.from_user.first_name
        user_id = message.from_user.id
        if content.startswith("/") or content.startswith("#"): return #
        await message.reply_text("<b>Your message has been sent to my moderators !</b>")
        await bot.send_message(
            chat_id=LOG_CHANNEL,
            text=f"<b>#PM_MSG\n\nName : {user}\n\nID : {user_id}\n\nMessage : {content}</b>"
        )



@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_text(client, message):
    if PM_MAINTENANCE_MODE:
        content = message.text
        user = message.from_user.mention
        if content.startswith("/"): return #
        await message.reply_text(text=(G_FILTER.format(user)), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡️ Backup Channel ⚡️",url="https://t.me/+FAgX05kGByNkZjJl"),]]),parse_mode=enums.ParseMode.HTML)  
        
