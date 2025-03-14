from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard_dict = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Календарь диктантов', url="https://vsekonkursy.ru/kalendar-diktantov-2021.html")],
                                                       [InlineKeyboardButton(text='Интерактивные IT диктанты', url="https://урокцифры.рф")],
                                                       ])

keyboard_chemp = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Московские мастера', url="https://prof.mcrpo.ru")],
                                                       [InlineKeyboardButton(text='Чемпионат высоких технологий', url="https://chvt.mcrpo.ru")],
                                                       [InlineKeyboardButton(text='Фуджиатлон', url="https://phygiathlon.ru")],
                                                       [InlineKeyboardButton(text='ArtMasters', url="https://artmasters.ru")],
                                                       ])

keyboard_konk = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Агрегатор конкурсов', url="https://конкурсы.рф/contests?filter%5Bcategory%5D%5B%5D=14")],
                                                       [InlineKeyboardButton(text='Муждународный конкурс цифровых решений', url="https://asi.ru/leaders/initiatives/data/")],
                                                       [InlineKeyboardButton(text='Международный конкурс по искуственному интеллекту Al Challtnge', url="https://aiijc.com/ru/")]
                                                       ])

keyboard_hacks = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Агрегатор хакатонов hackatons.pro', url="https://hackathons.pro")],
                                                       [InlineKeyboardButton(text='Агрегатор хакатонов хакатоны.рф', url="https://www.хакатоны.рф")]
                                                       ])

keyboard_ol = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Олимпиада "Парки, усадьбы, музеи"', url="https://museum.cpm.moscow")],
                                                       [InlineKeyboardButton(text='Олимпиада - ИТ планета', url="https://world-it-planet.org/challenges.html")],
                                                       [InlineKeyboardButton(text='Всероссийская олимпиада по искуственному интеллекту', url="https://ai.edu.gov.ru")],
                                                       ])

button1 = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Привет, КУИТ! Поехали!")]],
        resize_keyboard=True
    )

button2 = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Диктанты")],
                  [KeyboardButton(text="Конкурсы")],
                  [KeyboardButton(text="Хакатоны")],
                  [KeyboardButton(text="Чемпионаты")],
                  [KeyboardButton(text="Олимпиады")],
                  [KeyboardButton(text="Прикрепить достижения")]]
    )

achievements_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Прикрепить достижения', url='https://drive.google.com/drive/folders/1vsu7zeLIrDf4bNVJJpaK4G8Q8ADOiI1d')]
                                                       ])
