import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import os
from db.db import Database
import app.user_handlers as us_h

load_dotenv(".env")

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
database = Database("bot_db.db")




async def main():
    dp.include_routers(us_h.user_router)
    await dp.start_polling(bot, on_startup=await init_all())
    print("Start bot")


async def init_all():
    await database.initialize_database()
    print("Database initialized")



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('LOL')