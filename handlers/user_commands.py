from aiogram import Dispatcher
from menus import user_menus

def register_messages_client(dp: Dispatcher):
    dp.register_message_handler(user_menus.main_menu_menu,
                                commands=['start'])
