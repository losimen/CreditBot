from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage

import certifi
import config
import logging


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

connect_str = f"mongodb+srv://{config.MONGO_USERNAME}:{config.MONGO_PASS}@{config.MONGO_CLUSTER}/?retryWrites=true&w=majority"

storage = MongoStorage(
    uri=connect_str,
    tlsCAFile=certifi.where()
)


bot = Bot(token=config.BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage= storage)
