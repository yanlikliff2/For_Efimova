from run import bot
from run import database as db

from aiogram.fsm.state import StatesGroup, State
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputMediaDocument, FSInputFile

import app.keyboards as kb

import app.admin_keyboards as akb

user_router = Router()

VERSION = '0.0.1-beta'
DEVELOPERS = ['@npokhodnya', '@Volosatiyyy']


class Form(StatesGroup):
    start_broadcast = State()


start_text2 = (
    'Я предлагаю Вам различные мероприятия, которые помогут  определиться с выбором направления ваших интересов. '
    'Выберите, с чего мы начнем)')
start_text = (
    'Здравствуйте! Я бот КУИТ. Меня создал куратор группы - Ефимова Олеся Игоревна. Со мной можно с пользой провести время,'
    ' развиваться, обучаться,творить, самообразовываться и проверять свои знания.')


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    us_id = message.from_user.id
    await db.add_user(us_id, message.from_user.username)
    await bot.send_photo(photo="photos/photo_2025-03-14_21-13-58.jpg", caption=start_text,
                         reply_markup=kb.button1)


@user_router.callback_query(F.text == 'Привет, КУИТ! Поехали!')
async def hi(callback: CallbackQuery):
    await bot.send_photo(photo="photos/photo_2025-03-14_21-14-24.jpg", caption=start_text2,
                         reply_markup=kb.button1)
    await bot.send_photo(photo="photos/photo_2025-03-14_21-14-31.jpg",
                         caption="Напоминаю, после прохождения"
                                 "мероприятия обязательно зайдите в свою папку и прикрепите свой сертификат!",
                         reply_markup=kb.achievements_keyboard)


@user_router.callback_query(F.text == 'Диктанты')
async def page2(callback: CallbackQuery):
    await callback.message.answer('Диктанты',
                                  reply_markup=kb.keyboard_dict)


@user_router.callback_query(F.text == 'Викторины')
async def page2(callback: CallbackQuery):
    await callback.message.answer('Викторины',
                                  reply_markup=kb.keyboard_vict)


@user_router.callback_query(F.text == 'Викторины')
async def page2(callback: CallbackQuery):
    await callback.message.answer('Викторины',
                                  reply_markup=kb.keyboard_vict)
