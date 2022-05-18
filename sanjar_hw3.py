from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot
from keyboards.client_kb import cancel_marcup


class FSMAdmin(StatesGroup):
    names_of_dish = State()
    des_of_dish = State()
    price = State()
    over = State()


async def fsm_start(message: types.Message):
    if message.chat.type != 'private':
        await FSMAdmin.names_of_dish.set()
        await bot.send_message(
            message.chat.id,
            f"Привет {message.from_user.full_name}, скинь фотку блюду...",
            reply_markup=cancel_marcup
        )
    else:
        await message.answer("Пиши в личку!")


async def load_names_of_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['names_of_dish'] = message.photo[0].file_id
        print(data)
    await FSMAdmin.next()
    await message.answer("Как называется блюда? ")


async def load_des_of_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['des_of_dish'] = message.text
        print(data)
        await message.answer("Описании блюды")


async def load_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)
            print(data)
            await message.answer("Цена блюды ?")
    except:
        await message.answer("Тоько числа !!!")


async def load_over(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['over'] = message.text
        print(data)
        await message.answer(" Все свободен ?")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("Регистрация отменена!")


def register_hendler_fsmanketa(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands="cancel")
    dp.register_message_handler(cancel_registration, Text(equals='cancel',
                                                          ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['register'])
    dp.register_message_handler(load_names_of_dish, state=FSMAdmin.names_of_dish, content_types=["photo"])
    dp.register_message_handler(load_des_of_dish, state=FSMAdmin.des_of_dish)
    dp.register_message_handler(load_price, state=FSMAdmin.price)


