from aiogram import types
import keyboards.keyboards_generator.user_keyboards as keyboard_generator


async def welcome_user(message: types.Message):
    await message.answer(text='🇺🇦 Оберіть мову\n\n'
                              '🇷🇺 Выберите язык\n\n', reply_markup=keyboard_generator.welcome_user())