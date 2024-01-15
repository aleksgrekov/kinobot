from telebot.types import ReplyKeyboardMarkup, KeyboardButton

high_markup = ReplyKeyboardMarkup(resize_keyboard=True)
item1 = KeyboardButton('Самый высокий рейтинг сайта \"Кинопоиск\"')
item2 = KeyboardButton('Самый высокий рейтинг сайта \"IMDb\"')
item3 = KeyboardButton('Самые долгие фильмы')

high_markup.add(item1, item2, item3)

high_markup_dict = {item1.text: 'rating.kp',
                    item2.text: 'rating.imdb',
                    item3.text: 'movieLength'}
