from aiogram import Dispatcher, executor

from db.db import init_db
from excel import excel_generator
from loader import dp, bot
from config import ADMIN_ID

from handlers import user_commands
from FSM import expense_fsm
from FSM import income_fsm
from keyboards.callback_handlers import user_callbacks

user_commands.register_messages_client(dp)
expense_fsm.register_handlers_expense_fsm(dp)
user_callbacks.register_user_callback(dp)
income_fsm.register_handlers_income_fsm(dp)


async def on_startup(dp: Dispatcher):
    await init_db()
    excel_generator.init_folders()
    await bot.send_message(chat_id=ADMIN_ID,
                           text="Bot has started")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)