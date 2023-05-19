from aiogram import Dispatcher
from menus import user_menus
from FSM import income_fsm, expense_fsm


def register_messages_client(dp: Dispatcher):
    dp.register_message_handler(user_menus.main_menu_menu,
                                commands=['start'])
    dp.register_message_handler(income_fsm.fsm_start_income_form,
                                commands=['income'])
    dp.register_message_handler(expense_fsm.fsm_start_expense_form,
                                commands=['expense'])
