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


def date_controller_markup(user_id: int, date: str, isInfo: bool) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    day_up_button = types.InlineKeyboardButton(text="🔼",
                                               callback_data=f"controllerMenu_dayUp_{user_id}_{date}")
    day_down_button = types.InlineKeyboardButton(text="⬇️",
                                                 callback_data=f"controllerMenu_dayDown_{user_id}_{date}")

    mont_left_button = types.InlineKeyboardButton(text="⬅️",
                                                  callback_data=f"controllerMenu_monthLeft_{user_id}_{date}")
    mont_right_button = types.InlineKeyboardButton(text="➡️",
                                                   callback_data=f"controllerMenu_monthRight_{user_id}_{date}")

    keyboard.add(day_up_button)
    keyboard.add(mont_left_button, mont_right_button)
    keyboard.add(day_down_button)

    if not isInfo:
        get_info_button = types.InlineKeyboardButton(text="ℹ️ Отримати інформацію ℹ️",
                                                     callback_data=f"controllerMenu_getInfo_{user_id}_{date}")
        keyboard.add(get_info_button)

    return keyboard
