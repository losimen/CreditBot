from aiogram import Bot, Dispatcher
import config
import logging


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
