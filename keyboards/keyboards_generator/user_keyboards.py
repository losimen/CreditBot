from aiogram import types


def main_menu_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

    button_phone = types.InlineKeyboardButton(text='Hello world',
                                              callback_data='void')

    keyboard.add(button_phone)
    return keyboard
