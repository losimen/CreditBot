from aiogram import types
import keyboards.keyboards_generator.user_keyboards as keyboard_generator

from db.queries.insert_query import insert_user
from db.queries.get_query import get_user_data

async def main_menu_menu(message: types.Message):
    if not await get_user_data(message.from_user.id):
        await insert_user(message.from_user.id, message.from_user.first_name,
                          message.from_user.last_name, message.from_user.username)

    await message.answer(text='Головне <b>меню</b> 💸\n\n'
                              'Виберіть потрібний пункт меню 👇🏻',
                         reply_markup=keyboard_generator.main_menu_markup())
