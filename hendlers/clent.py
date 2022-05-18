from aiogram import types, Dispatcher
from config import dp,bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from keyboards import client_kb
dp = dp
# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Hey big bro {message.from_user.full_name}",
                        reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply(f"ИНСТРУКЦИЯ!")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Кто открыл Австралию ?"
    answers = ['1. Америго Веспучи', '2. Христофор Колумб', '3. Джеймс Кук', '4. Фернан Магелланн']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


def register_hendler_client(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(help, commands='help')
    dp.register_message_handler(quiz_1, commands='quiz_1')
