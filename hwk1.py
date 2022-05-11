from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import logging
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Hey big bro {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "В каком стране появился программирования ?"
    answers = ['1. Австралия', '2. США', '3. Кыргызстан', '4. Индия']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.message_handler(commands=['hendler'])
@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def hendler(call: types.CallbackQuery):


    question = "Сайтама"
    answers = []
    photo = open("images/ok_thumb.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='hendler',
        correct_option_id=1,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)






    # markup = InlineKeyboardMarkup()
    # button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    # markup.add(button_call_1)
    #
    # question = "Кто открыл Австралию ?"
    # answers = ['1. Христофор Колумб'
    #            '2. Джеймс Кук'
    #            '3. Америго Веспучи'
    #            '4. Фернан Магеллан']
    # await bot.send_poll(
    #     chat_id=message.from_user.id,
    #     question=question,
    #     options=answers,
    #     is_anonymous=False,
    #     type='quiz',
    #     correct_option_id=1,
    #     explanation="Это же легко",
    #     explanation_parse_mode=ParseMode.MARKDOWN_V2,
    #     reply_markup=markup
    # )













