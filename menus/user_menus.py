from aiogram import types
import keyboards.keyboards_generator.user_keyboards as keyboard_generator


async def main_menu_menu(message: types.Message):
    await message.answer(text='Головне <b>меню</b> 💸\n\n'
                              'Виберіть потрібний пункт меню 👇🏻',
                         reply_markup=keyboard_generator.main_menu_markup())