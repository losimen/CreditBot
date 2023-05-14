from aiogram import types


def main_menu_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    addExpense = types.InlineKeyboardButton(text='Додати витрату 📝',
                                            callback_data='mainMenu_addExpense')

    addIncome = types.InlineKeyboardButton(text='Додати прибуток 💰',
                                             callback_data='mainMenu_addIncome')

    showBalance = types.InlineKeyboardButton(text='Показати баланс 💵',
                                             callback_data='mainMenu_showBalance')

    keyboard.add(addExpense, addIncome)
    keyboard.add(showBalance)
    return keyboard
