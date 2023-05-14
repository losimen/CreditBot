from aiogram import Dispatcher, executor

from db.db import init_db
from loader import dp, bot
from config import ADMIN_ID
from handlers import user_commands


user_commands.register_messages_client(dp)

async def on_startup(dp: Dispatcher):
    await init_db()
    await bot.send_message(chat_id=ADMIN_ID,
                           text="Bot has started")

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)