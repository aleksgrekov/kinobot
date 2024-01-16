from telebot.types import Message
from telebot.apihelper import ApiTelegramException

from loader import bot
from database.models import User
from api.api import suggested_films


def check_registration(message: Message) -> bool:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return False
    else:
        return True


def get_films(message: Message, sort_type: int, limit: int, sort_field: str, range_value: str | None) -> None:
    bot.send_message(message.chat.id, 'Подборка может занять некоторое время. Ожидайте!😜')
    bot.send_chat_action(chat_id=message.chat.id,
                         action='upload_photo')
    movie_list = suggested_films(sort_type=sort_type, limit=limit, sort_field=sort_field, range_value=range_value)

    posters = [film.poster for film in movie_list]
    movies = map(str, movie_list)

    for poster, movie in zip(posters, movies):
        if poster:
            try:
                if len(movie) <= 1024:
                    bot.send_photo(message.chat.id, poster, caption=movie)
                else:
                    bot.send_photo(message.chat.id, poster)
                    bot.send_message(message.chat.id, movie)
            except ApiTelegramException:
                bot.send_message(message.chat.id, movie)
        else:
            bot.send_message(message.chat.id, movie)
