from telebot.types import Message

from loader import bot
from api.api import suggested_films


def get_films(message: Message, sort_type: int) -> None:
    bot.send_message(message.chat.id, 'Подборка может занять некоторое время. Ожидайте!😜')
    bot.send_chat_action(chat_id=message.chat.id,
                         action='upload_photo')
    movie_list = suggested_films(sort_type)

    posters = [film.poster for film in movie_list]
    movies = map(str, movie_list)

    for poster, movie in zip(posters, movies):
        if poster:
            if len(movie) <= 1024:
                bot.send_photo(message.chat.id, poster, caption=movie)
            else:
                bot.send_photo(message.chat.id, poster)
                bot.send_message(message.chat.id, movie)
        else:
            bot.send_message(message.chat.id, movie)


@bot.message_handler(commands=['high'])
def send_high(message: Message) -> None:
    get_films(message=message, sort_type=-1)


@bot.message_handler(commands=['low'])
def send_low(message: Message) -> None:
    get_films(message=message, sort_type=1)


@bot.message_handler(func=lambda message: True)
def greetings(message: Message) -> None:
    user_name = message.from_user.first_name
    bot.send_chat_action(chat_id=message.chat.id,
                         action='typing')
    bot.reply_to(message,
                 '{name}, для работы выбери доступную команду из меню или введи команду '
                 '/help, чтобы узнать больше о моих возможностях.'.format(name=user_name))
