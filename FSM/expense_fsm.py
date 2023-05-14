from aiogram.dispatcher.filters.state import StatesGroup, State


class ExpenseFSM(StatesGroup):
    expense_reason = State()
    expense_amount = State()


