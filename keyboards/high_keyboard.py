from telebot.types import ReplyKeyboardMarkup, KeyboardButton

"""
Модуль, содержащий настройки клавиатуры для команды /high.

Переменные:
- high_markup: Экземпляр ReplyKeyboardMarkup для клавиатуры.
- item1: Элемент клавиатуры для выбора подборки с самым высоким рейтингом сайта "Кинопоиск".
- item2: Элемент клавиатуры для выбора подборки с самым высоким рейтингом сайта "IMDb".
- item3: Элемент клавиатуры для выбора подборки с самыми долгими фильмами.

high_markup_dict: Словарь, связывающий текст элемента клавиатуры с соответствующим значением для запроса.

"""

high_markup = ReplyKeyboardMarkup(resize_keyboard=True)
item1 = KeyboardButton('Самый высокий рейтинг сайта \"Кинопоиск\"')
item2 = KeyboardButton('Самый высокий рейтинг сайта \"IMDb\"')
item3 = KeyboardButton('Самые долгие фильмы')

high_markup.add(item1, item2, item3)

high_markup_dict = {item1.text: 'rating.kp',
                    item2.text: 'rating.imdb',
                    item3.text: 'movieLength'}
