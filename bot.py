from aiogram.utils import executor
from config import TOKEN
from create_bot import dp, bot
from handlers import processor
from logger import logging



async def on_startup(_):
    print("Бот онлайн")
    logging.info('Start')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)