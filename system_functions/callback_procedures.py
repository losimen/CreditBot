from aiogram import types

from db.queries.get_query import get_user_history_for_month
from loader import logger

from menus import user_menus
from system_functions.date_worker import extract_days, change_day, get_str_datetime
from helpers import roll_switcher


async def delete_message(callback: types.CallbackQuery):
    try:
        await callback.message.delete()
    except:
        logger.debug(f"BOT - {callback.message.chat.id} was not active more than 48 hours")


async def switch_day(message, is_up, user_id, date):
    history = await get_user_history_for_month(user_id, date)
    days = list(sorted(extract_days([get_str_datetime(x.date) for x in history])))

    if len(days) == 0:
        await user_menus.user_statistic_menu(message, user_id, date)
        return

    input_day = list(extract_days([date]))[0]

    try:
        index_input_day = days.index(input_day)
    except ValueError:
        index_input_day = -1

    new_day = days[roll_switcher(is_up, index_input_day, len(days))]

    await user_menus.user_statistic_menu(message, user_id, change_day(date, new_day))
