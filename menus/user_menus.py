from aiogram import types
import keyboards.keyboards_generator.user_keyboards as keyboard_generator

from db.queries.insert_query import insert_user
from db.queries.get_query import get_user_data

from db.types.user_data import UserData
from helpers import generate_user_history_days


async def main_menu_menu(message: types.Message):
    user_data = await get_user_data(message.from_user.id)
    if not user_data:
        user_data = UserData(message.from_user.id, message.from_user.first_name,
                             message.from_user.last_name, message.from_user.username)
        await insert_user(user_data)

    await message.answer(text='Головне <b>меню</b> 💸\n\n'
                              'Виберіть потрібний пункт меню 👇🏻',
                         reply_markup=keyboard_generator.main_menu_markup())
async def user_balance_menu(message: types.Message, user_id: int, date: str):
    await message.answer(text=f"{await generate_user_history_days(user_id, date)}\n\n",
                         reply_markup=keyboard_generator.date_controller_markup(user_id, date, False))
