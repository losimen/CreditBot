import datetime

from aiogram import types
import keyboards.keyboards_generator.user_keyboards as keyboard_generator
import excel.excel_generator as excel_generator

from db.queries.insert_query import insert_user
from db.queries.get_query import get_user_data, get_user_history_for_all_time
from db.types.user_data import UserData
from helpers import generate_user_history_days, type_report
from system_functions.date_worker import get_current_datetime


async def main_menu_menu(message: types.Message):
    print('start - ', message.chat.id, ' | ', datetime.datetime.now())
    user_data = await get_user_data(message.chat.id)
    if not user_data:
        user_data = UserData(message.chat.id, message.chat.first_name,
                             message.chat.last_name, message.chat.username)
        await insert_user(user_data)

    await message.answer(text='Головне <b>меню:</b> 💸\n\n'
                              'Виберіть потрібний пункт меню 👇🏻',
                         reply_markup=keyboard_generator.main_menu_markup())


async def user_statistic_menu(message: types.Message, user_id: int, date: str):
    await message.answer(text=f"{await generate_user_history_days(user_id, date)}\n\n",
                         reply_markup=keyboard_generator.date_controller_markup(user_id, date, False))


async def user_profile_menu(message: types.Message):
    user_data = await get_user_data(message.chat.id)

    await message.answer(text='Ваш <b>профіль:</b> 🧑🏻‍💻\n\n'
                              f'<b>Ваш баланс:</b> <code>{user_data.balance}</code> 🪙\n',
                         reply_markup=keyboard_generator.user_profile_markup())


async def user_report_menu(message: types.Message):
    await message.answer(text='Оберіть найбільш <b>зручний</b> для вас <b>звіт</b> за <b>весь</b> час 📊\n\n'
                              'Виберіть потрібний пункт меню 👇🏻',
                         reply_markup=keyboard_generator.user_report_markup())


async def user_report_menu_report(message: types.Message, type: str):
    data_all = await get_user_history_for_all_time(message.chat.id)
    if type == 'date':
        data_all = sorted(data_all, key=lambda x: x.date)
    if type == 'amount':
        data_all = sorted(data_all, key=lambda x: int(x.amount))[::-1]

    excel_generator.create_file(message.chat.id, data_all, type)
    await message.answer_document(document=open(f'./reports/{type}-{message.chat.id}.xlsx', 'rb'), caption=f'<b>{type_report[type]}</b> - {get_current_datetime()[:-13]}')
    await main_menu_menu(message)