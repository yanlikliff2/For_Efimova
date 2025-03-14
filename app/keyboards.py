from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard_dict = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ГМЦ', url="")],
                                                       [InlineKeyboardButton(text='Сайты о диктантах', url="")],
                                                       [InlineKeyboardButton(text='Интерактивный диктант', url="")],
                                                       [InlineKeyboardButton(text='Онлайн-диктант', url="")]
                                                       ])

keyboard_vict = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='ГМЦ', url="")],
                                                       [InlineKeyboardButton(text='День России', url="")]
                                                       ])

button1 = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Привет, КУИТ! Поехали!")]],
        resize_keyboard=True
    )

button2 = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Диктанты")],
                  [KeyboardButton(text="Викторины")],
                  [KeyboardButton(text="Конкурсы")],
                  [KeyboardButton(text="Олимпиады")],
                  [KeyboardButton(text="Музеи")],
                  [KeyboardButton(text="Группы")]]
    )

achievements_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Достижения', callback_data='Заглушка')]
                                                       ])