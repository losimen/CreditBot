from db.db import collection_users_data
from db.db import collection_expenses

from db.types.user_data import UserData
from db.types.expense import Expense

async def insert_user(user_data: UserData) -> None:
    await collection_users_data.insert_one(user_data.to_dict())

async def insert_expense(expense: Expense) -> None:
    await collection_expenses.insert_one(expense.to_dict())
