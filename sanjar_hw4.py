import sqlite3
import random
from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")
    db.execute("CREATE TABLE IF NOT EXISTS menu "
               "(id INTEGER PRIMARY KEY, dish_name TEXT,"
               "recipe TEXT, name TEXT, price TEXT,"
               "over INTEGER)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO  VALUES menu"
                       "(?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_user = random.randint(0, len(result) - 1)
    await bot.send_photo(message.from_user.id,
                         result[random_user][2],
                         caption= f"Dish's name: {result[random_user][3]}\n"
                                   f"Recipe name: {result[random_user][4]}\n"
                                   f"Price : {result[random_user][5]}\n"
                                   f"Over : {result[random_user][6]}\n\n"
                                   f"{result[random_user][1]}\n")

async def sql_command_all():
    return cursor.execute("SELECT * FROM menu").fetchall()

async def sql_command_delete(id):
    cursor.execute("DELETE FROM menu WHERE id == ?", (id,))
    db.commit()



