from telebot.types import Message

from loader import bot
# from api.test_api import suggested_films
from api.api import suggested_films


@bot.message_handler(commands=['high'])
def send_high(message: Message) -> None:
    movie_list = suggested_films(-1)
    movies = map(str, movie_list)
    for movie in movies:
        bot.send_message(message.chat.id, movie)


@bot.message_handler(commands=['low'])
def send_low(message: Message) -> None:
    movie_list = suggested_films(1)
    movies = map(str, movie_list)
    for movie in movies:
        bot.send_message(message.chat.id, movie)


@bot.message_handler(func=lambda message: True)
def greetings(message: Message) -> None:
    user_name = message.from_user.first_name
    bot.reply_to(message,
                 '{name}, для работы выбери доступную команду из меню или введи команду '
                 '/help, чтобы узнать больше о моих возможностях.'.format(name=user_name))
