from telebot.types import ReplyKeyboardMarkup, KeyboardButton

"""
Модуль, содержащий настройки клавиатуры для команды /custom.

Переменные:
- custom_markup: Экземпляр ReplyKeyboardMarkup для клавиатуры.
- item1: Элемент клавиатуры для выбора года выхода фильма.
- item2: Элемент клавиатуры для выбора диапазона рейтинга Кинопоиск.

custom_markup_dict: Словарь, связывающий текст элемента клавиатуры с соответствующим значением для запроса.

"""

custom_markup = ReplyKeyboardMarkup(resize_keyboard=True)
item1 = KeyboardButton('Год(а) выхода фильма')
item2 = KeyboardButton('Диапазон рейтинга Кинопоиск')

custom_markup.add(item1, item2)

custom_markup_dict = {item1.text: 'year',
                      item2.text: 'rating.kp'}
