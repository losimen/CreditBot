from aiogram.dispatcher.filters import Text
from aiogram import types

from helpers import generate_user_history_day
from loader import bot

from FSM.expense_fsm import fsm_start_expense_form
from FSM.income_fsm import fsm_start_income_form
from menus import user_menus
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

    if callback_data == 'mainMenu':
        await user_menus.main_menu_menu(callback.message)
    elif callback_data == 'mainMenu_addExpense':
        await fsm_start_expense_form(callback.message)
    elif callback_data == 'mainMenu_addIncome':
        await fsm_start_income_form(callback.message)
    elif callback_data == 'mainMenu_profile':
        await user_menus.user_profile_menu(callback.message)


async def controller_menu_callback(callback: types.CallbackQuery):
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
        await callback.message.answer(
            text=f"{callback.message.text}\n\n {await generate_user_history_day(str(user_id), date)}",
            reply_markup=user_menus.keyboard_generator.date_controller_markup(user_id, date, True))
    elif call_ == 'monthRight':
        await user_menus.user_statistic_menu(callback.message, user_id, add_months(date, 1))
    elif call_ == 'monthLeft':
        await user_menus.user_statistic_menu(callback.message, user_id, add_months(date, -1))


async def user_profile_menu_callback(callback: types.CallbackQuery):
    await delete_message(callback.message)

    if callback.data == 'userProfileMenu':
        await user_menus.user_profile_menu(callback.message)
    elif callback.data == 'userProfileMenu_showStatistic':
        date = get_current_datetime()
        await user_menus.user_statistic_menu(callback.message, callback.message.chat.id, date)
    elif callback.data == 'userProfileMenu_reportAllTime':
        await user_menus.user_report_menu(callback.message)


async def user_report_menu_callback(callback: types.CallbackQuery):
    await delete_message(callback.message)

    if callback.data == 'userReportMenu':
        await user_menus.user_report_menu(callback.message)
    elif callback.data == "userReportMenu_defaultReport":
        await user_menus.user_report_menu_report(callback.message, 'default')
    elif callback.data == "userReportMenu_sortByDate":
        await user_menus.user_report_menu_report(callback.message, 'date')
    elif callback.data == "userReportMenu_sortByBalance":
        await user_menus.user_report_menu_report(callback.message, 'amount')


def register_user_callback(dp):
    dp.register_callback_query_handler(main_menu_callback, Text(startswith='mainMenu'))
    dp.register_callback_query_handler(controller_menu_callback, Text(startswith='controllerMenu'))
    dp.register_callback_query_handler(user_profile_menu_callback, Text(startswith='userProfileMenu'))
    dp.register_callback_query_handler(user_report_menu_callback, Text(startswith='userReportMenu'))
    dp.register_callback_query_handler(void_call, Text(startswith='void'))
