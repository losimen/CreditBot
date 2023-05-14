from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types, Dispatcher

from db.types.expense import Expense
from db.queries.insert_query import insert_expense

from menus.user_menus import main_menu_menu

class ExpenseFSM(StatesGroup):
    expense_description = State()
    expense_amount = State()


async def fsm_start_expense_form(message: types.Message):
    await message.answer(text='Введіть <b>опис</b> витрати 👇🏻\n'
                              '<i>колись добавлю теги</i>')
    await ExpenseFSM.expense_description.set()


async def fsm_expense_description(message: types.Message, state: FSMContext):
    await state.update_data(expense_description=message.text)
    await message.answer(text='Введіть <b>суму</b> витрати 👇🏻')
    await ExpenseFSM.expense_amount.set()


async def fsm_expense_amount(message: types.Message, state: FSMContext):
    await state.update_data(expense_amount=message.text)
    await message.answer(text='Витрата <b>додана</b> ✅')
    data = await state.get_data()

    expense = Expense(message.from_user.id, data['expense_amount'], data['expense_description'], message.date)
    await insert_expense(expense)

    await state.finish()
    await main_menu_menu(message)


def register_handlers_expense_fsm(dp: Dispatcher):
    dp.register_message_handler(fsm_start_expense_form, state=None, commands='expense')
    dp.register_message_handler(fsm_expense_description, state=ExpenseFSM.expense_description)
    dp.register_message_handler(fsm_expense_amount, state=ExpenseFSM.expense_amount)
