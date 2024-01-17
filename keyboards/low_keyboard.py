from telebot.types import ReplyKeyboardMarkup, KeyboardButton

"""
Модуль, содержащий настройки клавиатуры для команды /high.

Переменные:
- low_markup: Экземпляр ReplyKeyboardMarkup для клавиатуры.
- item1: Элемент клавиатуры для выбора подборки с самым низким возрастным рейтингом.
- item2: Элемент клавиатуры для выбора подборки с самыми старыми фильмами.
- item3: Элемент клавиатуры для выбора подборки с самыми короткими фильмами.

low_markup_dict: Словарь, связывающий текст элемента клавиатуры с соответствующим значением для запроса.

"""

low_markup = ReplyKeyboardMarkup(resize_keyboard=True)
item1 = KeyboardButton('Самый низкий возрастной рейтинг')
item2 = KeyboardButton('Самые старые фильмы')
item3 = KeyboardButton('Самые короткие фильмы')

low_markup.add(item1, item2, item3)

low_markup_dict = {item1.text: 'ageRating',
                   item2.text: 'year',
                   item3.text: 'movieLength'}
