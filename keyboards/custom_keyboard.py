from telebot.types import ReplyKeyboardMarkup, KeyboardButton

custom_markup = ReplyKeyboardMarkup(resize_keyboard=True)
item1 = KeyboardButton('Период времени')
item2 = KeyboardButton('Диапазон рейтинга Кинопоиск')

custom_markup.add(item1, item2)

custom_markup_dict = {item1.text: 'rating.kp',
                      item2.text: 'rating.imdb'}
