from aiogram import types, Dispatcher
from config import bot, ADMIN

async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id != ADMIN:
            await message.reply("You aren't my boss!")
        if not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")
        else:
            await message.bot.kick_chat_member(message.chat.id,
                                               user_id=message.reply_to_message.from_user.id)
            await bot.send_message(
                message.chat.id,
                f"{message.reply_to_message.from_user.full_name}"
                f"was a ban {message.from_user.full_name}"
            )
    else:
        await message.answer("Это работает только в группах!")


def register_hendler_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/*")