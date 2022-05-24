import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="Got your id")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Gotta sleep!")


async def wake_up():
    file = open("images/Cheese People - Wake Up (Lyrics) _hey come on you lazy wake up, hey come on take your drums_ Tiktok.mp4," "rb")
    await bot.send_video(chat_id=chat_id, video=file, caption="Wake Up Sanjar! ")


async def scheduler():
    aioschedule.every().day.fr("20:00").do(go_to_sleep)
    aioschedule.every().day.monday("06:00").do(wake_up)
    aioschedule.every().day.sunday("06:00").do(wake_up)
    aioschedule.every().day.thursday("06:00").do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'wake up' in word)


