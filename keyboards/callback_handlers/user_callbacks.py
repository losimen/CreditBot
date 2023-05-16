from aiogram.dispatcher.filters import Text
from aiogram import types

from helpers import generate_user_history_day
from loader import dp, bot

from FSM.expense_fsm import fsm_start_expense_form
from FSM.income_fsm import fsm_start_income_form
from menus import user_menus
from menus.user_menus import user_balance_menu
from system_functions.callback_procedures import switch_day
from system_functions.date_worker import get_current_datetime, add_months


async def delete_message(message: types.Message):
    try:
        await message.delete()
    except:
        pass


async def void_call(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id, text='Ця кнопка нічого не робить 😅')

async def main_menu_callback(callback: types.CallbackQuery):
    await callback.message.delete()
    callback_data = callback.data

    if callback_data == 'mainMenu_addExpense':
        await fsm_start_expense_form(callback.message)
    elif callback_data == 'mainMenu_addIncome':
        await fsm_start_income_form(callback.message)
    elif callback_data == 'mainMenu_showBalance':
        date = get_current_datetime()
        await user_balance_menu(callback.message, callback.from_user.id, date)

@dp.callback_query_handler(Text(startswith='controllerMenu'))
async def controller_menu(callback: types.CallbackQuery):
    await delete_message(callback.message)

    split_call = callback.data.split('_')
    call_ = split_call[1]
    user_id = int(split_call[2])
    date = split_call[3]

    if call_ == 'dayUp':
        await switch_day(callback.message, True, user_id, date)
    elif call_ == 'dayDown':
        await switch_day(callback.message, False, user_id, date)
    elif call_ == 'getInfo':
        await callback.message.answer(text=f"{callback.message.text}\n\n {await generate_user_history_day(str(user_id), date)}",
                                      reply_markup=user_menus.keyboard_generator.date_controller_markup(user_id, date, True))
    elif call_ == 'monthRight':
        await user_menus.user_balance_menu(callback.message, user_id, add_months(date, 1))
    elif call_ == 'monthLeft':
        await user_menus.user_balance_menu(callback.message, user_id, add_months(date, -1))

def register_user_callback(dp):
    dp.register_callback_query_handler(main_menu_callback, Text(startswith='mainMenu'))
    dp.register_callback_query_handler(void_call, Text(startswith='void'))