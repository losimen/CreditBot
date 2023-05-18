from db.db import collection_users_data, collection_incomes, collection_expenses
from db.types.expense import Expense
from db.types.income import Income

from db.types.user_data import UserData
from system_functions.date_worker import extract_month, extract_year, extract_day


async def get_user_data(user_id) -> UserData:
    user_data = None
    try:
        user_info = await collection_users_data.find_one({"_id": user_id})
        user_data = UserData.from_dict(user_info)
        return user_data
    except TypeError:
        return user_data


async def get_user_incomes_for_month(user_id, date) -> list:
    year = int(extract_year(date))
    month = int(extract_month(date))
    incomes = []
    async for income in collection_incomes.find({"user_id": int(user_id)}):
        inc = Income.from_dict(income)
        if inc.date.year == year and inc.date.month == month:
            incomes.append(inc)
    return incomes


async def get_user_incomes_for_day(user_id, date) -> list:
    year = int(extract_year(date))
    month = int(extract_month(date))
    day = int(extract_day(date))
    incomes = []
    async for income in collection_incomes.find({"user_id": int(user_id)}):
        inc = Income.from_dict(income)
        if inc.date.year == year and inc.date.month == month and inc.date.day == day:
            incomes.append(inc)
    return incomes


async def get_user_expense_for_month(user_id, date) -> list:
    year = int(extract_year(date))
    month = int(extract_month(date))
    expenses = []
    async for expense in collection_expenses.find({"user_id": int(user_id)}):
        exp = Expense.from_dict(expense)
        if exp.date.year == year and exp.date.month == month:
            expenses.append(exp)
    return expenses


async def get_user_expenses_for_day(user_id, date) -> list:
    year = int(extract_year(date))
    month = int(extract_month(date))
    day = int(extract_day(date))
    expenses = []
    async for expense in collection_expenses.find({"user_id": int(user_id)}):
        exp = Expense.from_dict(expense)
        if exp.date.year == year and exp.date.month == month and exp.date.day == day:
            expenses.append(exp)
    return expenses


async def get_user_history_for_month(user_id, date) -> list:
    history = []
    history.extend(await get_user_incomes_for_month(user_id, date))
    history.extend(await get_user_expense_for_month(user_id, date))
    return history


async def get_user_incomes_for_all_time(user_id) -> list:
    incomes = []
    async for income in collection_incomes.find({"user_id": int(user_id)}):
        incomes.append(Income.from_dict(income))
    return incomes


async def get_user_expenses_for_all_time(user_id) -> list:
    expenses = []
    async for expense in collection_expenses.find({"user_id": int(user_id)}):
        exp = Expense.from_dict(expense)
        exp.amount = "-" + exp.amount
        expenses.append(exp)
    return expenses


async def get_user_history_for_all_time(user_id) -> list:
    history = []
    history.extend(await get_user_incomes_for_all_time(user_id))
    history.extend(await get_user_expenses_for_all_time(user_id))
    return history
