from telebot.types import ReplyKeyboardMarkup, KeyboardButton

low_markup = ReplyKeyboardMarkup(resize_keyboard=True)
item1 = KeyboardButton('Самый низкий возрастной рейтинг')
item2 = KeyboardButton('Самые старые фильмы')
item3 = KeyboardButton('Самые короткие фильмы')

low_markup.add(item1, item2, item3)

low_markup_dict = {item1.text: 'ageRating',
                   item2.text: 'year',
                   item3.text: 'movieLength'}
