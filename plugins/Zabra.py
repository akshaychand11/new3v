








@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_filter(client, message):
    if PM_MAINTENANCE_MODE:
        if AUTH_USERS and message.from_user and message.from_user.id in AUTH_USERS:
            k = await manual_filters(client, message)
            if k == False:
                await auto_filter(client, message)
        else:
            await message.reply_text(text=(G_FILTER.format(message.from_user.mention)), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡️ Backup Channel ⚡️",url="https://t.me/+FAgX05kGByNkZjJl"),]]),parse_mode=enums.ParseMode.HTML)#"You are now verified for next 24 hours. Continue asking movies")      


