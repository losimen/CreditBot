from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types, Dispatcher
from db.types.income import Income
from db.queries.insert_query import insert_income
from db.queries.get_query import get_user_data
from db.queries.update_query import update_user_balance
from menus.user_menus import main_menu_menu


class IncomeFSM(StatesGroup):
    income_description = State()
    income_amount = State()


async def fsm_start_income_form(message: types.Message):
    await message.answer(text='Введіть <b>опис</b> доходу 👇🏻\n'
                              '<i>колись добавлю теги</i>')
    await IncomeFSM.income_description.set()


async def fsm_income_description(message: types.Message, state: FSMContext):
    await state.update_data(income_description=message.text)
    await message.answer(text='Введіть <b>суму</b> доходу 👇🏻')
    await IncomeFSM.income_amount.set()


async def fsm_income_amount(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(text='Введіть <b>число</b> 🙄')
        return

    await state.update_data(income_amount=message.text)
    await message.answer(text='Дохід <b>додано</b> ✅')
    data = await state.get_data()

    income = Income(message.chat.id, data['income_amount'], data['income_description'], message.date)
    user_data = await get_user_data(message.chat.id)

    await insert_income(income)
    await update_user_balance(message.chat.id, float(data['income_amount']) + float(user_data.balance))

    await state.finish()
    await main_menu_menu(message)


def register_handlers_income_fsm(dp: Dispatcher):
    dp.register_message_handler(fsm_start_income_form, state=None, commands='income')
    dp.register_message_handler(fsm_income_description, state=IncomeFSM.income_description)
    dp.register_message_handler(fsm_income_amount, state=IncomeFSM.income_amount)
