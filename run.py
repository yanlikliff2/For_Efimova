import asyncio
import logging
from multiprocessing import Process
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import os
from db.db import Database
import app.user_handlers as us_h
import aioschedule
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
parser = Parser(browser="firefox")
database = Database("bot_db.db")




async def main():
    from app.user_handlers import user_router
    from app.admin_handlers import admin_router
    logger.critical("START BOT")
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot, on_startup=await init_all())


async def init_all():
    await database.initialize_database()



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('LOL')