from db.queries.get_query import get_user_incomes_for_day, get_user_history_for_month, get_user_expenses_for_day
from system_functions.date_worker import extract_days, extract_month_name, extract_year, get_str_datetime, extract_time


async def generate_user_history_days(user_id: int, date: str):
    history = await get_user_history_for_month(user_id, date)

    days = sorted(extract_days([get_str_datetime(x.date) for x in history]))
    input_day = list(extract_days([date]))[0]

    days_text = ""
    for (index, day) in enumerate(days):
        if input_day == day:
            days_text += f"➡️ Ти тут ({day})\n"
        else:
            days_text += f"📅 {index+1}. {day}\n"

    if len(days) == 0:
        days_text += f"⚠️ <b>Немає</b> інформації на цей місяць"

    text = f"<b>{extract_month_name(date)} {extract_year(date)}</b>\n\n" \
           f"🔍 Дні, які я <b>знайшов</b> для вибраного місяця:\n" \
           f"{days_text}"

    return text

async def generate_user_history_day(user_id: str, date: str):
    history_income = await get_user_incomes_for_day(user_id, date)
    history_expense = await get_user_expenses_for_day(user_id, date)

    day_text = ""
    if len(history_income) == 0 and len(history_expense) == 0:
        day_text += f"⚠️ <b>Немає</b> інформації на цей день"
    else:
        day_text += f"- 💸<b>Доходи:</b>\n"
        day_income = 0

        if len(history_income) == 0:
            day_text += f"😔 <b>Немає</b> доходів на цей день\n\n"
        else:
            for index, income in enumerate(history_income):
                day_text += f" <b>[{index+1}]</b> {income.description}  <code>+{income.amount}</code>🪙  \n"
                day_income += int(income.amount)
            day_text += f"\n📈 Загальні доходи: <b>+{day_income}</b>🪙\n\n"

        day_text += f"- 🧑🏿‍🦱<b>Витрати:</b>\n"
        day_expense = 0

        if len(history_expense) == 0:
            day_text += f"🥳 <b>Немає</b> витрат на цей день"
        else:
            for index, expense in enumerate(history_expense):
                day_text += f" <b>[{index+1}]</b> {expense.description} <code>-{expense.amount}</code>🪙  \n"
                day_expense += int(expense.amount)
            day_text += f"\n📉 Загальні витрати: <b>-{day_expense}</b>🪙\n\n"

        day_text += f"📊Баланс за день: <b>{(day_income - day_expense):+}</b>🪙"

    text = f"⬇️ Інформація, яку я <b>знайшов</b> за <b>{date.split(' ')[0]}</b> ⬇️\n\n{day_text}️"
    return text


def roll_switcher(is_plus, current_index, len_of_list):
    if current_index == -1:
        return 0

    if is_plus:
        if current_index == 0:
            future_link = len_of_list - 1
        else:
            future_link = current_index - 1
    else:
        if current_index == len_of_list-1:
            future_link = 0
        else:
            future_link = current_index + 1

    return future_link
