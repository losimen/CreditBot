from aiogram.dispatcher.filters import Text
from aiogram import types

from loader import dp, logger

from FSM.expense_fsm import fsm_start_expense_form

async def delete_message(message: types.Message):
    try:
        await message.delete()
    except:
        pass


async def void_call(callback: types.CallbackQuery):
    pass


async def main_menu_callback(callback: types.CallbackQuery):
    await callback.message.delete()
    callback_data = callback.data

    if callback_data == 'mainMenu_addExpense':
        await fsm_start_expense_form(callback.message)
    elif callback_data == 'mainMenu_addIncome':
        pass
    elif callback_data == 'mainMenu_showBalance':
        pass


def register_user_callback(dp):
    dp.register_callback_query_handler(main_menu_callback, Text(startswith='mainMenu'))
    dp.register_callback_query_handler(void_call, Text(startswith='void'))