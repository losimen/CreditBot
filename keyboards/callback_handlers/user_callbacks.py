from loader import dp, logger
from aiogram.dispatcher.filters import Text
from menus import user_menus
from keyboards.keyboards_generator import user_keyboards
from aiogram import types


async def delete_message(message: types.Message):
    try:
        await message.delete()
    except:
        pass


@dp.callback_query_handler(text = 'void')
async def void_call(callback: types.CallbackQuery):
    pass


@dp.callback_query_handler(Text(startswith='mainMenu_'))
async def main_menu_callback(callback: types.CallbackQuery):
    await callback.message.delete()
    callback_data = callback.data

    if callback_data == 'mainMenu_addExpense':
        pass
    elif callback_data == 'mainMenu_addIncome':
        pass
    elif callback_data == 'mainMenu_showBalance':
        pass
