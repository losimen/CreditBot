from aiogram import types


def main_menu_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    addExpense = types.InlineKeyboardButton(text='Додати витрату 📝',
                                            callback_data='mainMenu_addExpense')

    addIncome = types.InlineKeyboardButton(text='Додати прибуток 💰',
                                           callback_data='mainMenu_addIncome')

    profile = types.InlineKeyboardButton(text='Профіль 🧑‍💻',
                                         callback_data='mainMenu_profile')

    keyboard.add(addExpense, addIncome)
    keyboard.add(profile)
    return keyboard


def date_controller_markup(user_id: int, date: str, is_info: bool) -> types.InlineKeyboardMarkup:
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

    if not is_info:
        get_info_button = types.InlineKeyboardButton(text="ℹ️ Отримати інформацію ℹ️",
                                                     callback_data=f"controllerMenu_getInfo_{user_id}_{date}")
        keyboard.add(get_info_button)
    else:
        keyboard.add(types.InlineKeyboardButton(text=f"Інформація за {date.split(' ')[0]}",
                                                callback_data="void"))

    keyboard.add(types.InlineKeyboardButton(text="< Назад",
                                            callback_data="userProfileMenu"))

    return keyboard


def user_profile_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    showBalance = types.InlineKeyboardButton(text='Денна статистика 📊',
                                             callback_data='userProfileMenu_showStatistic')
    reportAllTime = types.InlineKeyboardButton(text='Звіт за весь час 📅',
                                               callback_data='userProfileMenu_reportAllTime')
    back = types.InlineKeyboardButton(text="< Назад",
                                      callback_data="mainMenu")

    keyboard.add(showBalance)
    keyboard.add(reportAllTime)
    keyboard.add(back)

    return keyboard


def user_report_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    defaultReport = types.InlineKeyboardButton(text='Звичайний звіт 📄',
                                               callback_data='userReportMenu_defaultReport')
    sortByDate = types.InlineKeyboardButton(text='Сортування за датою 📅',
                                            callback_data='userReportMenu_sortByDate')
    sortByBalance = types.InlineKeyboardButton(text='Сортування за кількістю 🪙',
                                               callback_data='userReportMenu_sortByBalance')

    back = types.InlineKeyboardButton(text="< Назад",
                                      callback_data="userProfileMenu")

    keyboard.add(defaultReport)
    keyboard.add(sortByDate)
    keyboard.add(sortByBalance)
    keyboard.add(back)

    return keyboard
