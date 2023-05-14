from loader import dp, logger
from aiogram.dispatcher.filters import Text
from menus import user_menus
from aiogram import types

@dp.callback_query_handler(text = 'void')
async def void_call(callback: types.CallbackQuery):
    print('hello')
