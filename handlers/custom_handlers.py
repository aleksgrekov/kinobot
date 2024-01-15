from typing import Dict
from telebot.types import Message

from loader import bot
from api.api import suggested_films
from states.states import States
from keyboards import high_keyboard, low_keyboard, custom_keyboard


def go_to_count(message: Message, sort_type: int, markup: Dict[str, str]) -> None:
    if message.text not in markup:
        bot.reply_to(message,
                     'Не нужно самодеятельности!😁 Нажми на кнопку и выбери подборку, которую ты хочешь получить! 👇')
        return
    bot.reply_to(message, 'Из скольки фильмов ты будешь выбирать? Введи число от 1 до 10')
    bot.set_state(message.from_user.id, States.count, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['from_markup'] = message.text
        film_data['sort_type'] = sort_type
        film_data['markup'] = markup


def get_films(message: Message, sort_type: int, limit: int, sort_field: str) -> None:
    bot.send_message(message.chat.id, 'Подборка может занять некоторое время. Ожидайте!😜')
    bot.send_chat_action(chat_id=message.chat.id,
                         action='upload_photo')
    movie_list = suggested_films(sort_type=sort_type, limit=limit, sort_field=sort_field)

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
    bot.send_message(message.chat.id, 'Нажми на кнопку и выбери подборку, которую ты хочешь получить! 👇',
                     reply_markup=high_keyboard.high_markup)
    bot.set_state(message.from_user.id, States.high_type, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['state'] = States.high_type


@bot.message_handler(state=States.high_type)
def state_high(message: Message) -> None:
    go_to_count(message=message, sort_type=-1, markup=high_keyboard.high_markup_dict)


@bot.message_handler(commands=['low'])
def send_low(message: Message) -> None:
    bot.send_message(message.chat.id, 'Нажми на кнопку и выбери подборку, которую ты хочешь получить! 👇',
                     reply_markup=low_keyboard.low_markup)
    bot.set_state(message.from_user.id, States.low_type, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['state'] = States.low_type


@bot.message_handler(state=States.low_type)
def state_low(message: Message) -> None:
    go_to_count(message=message, sort_type=1, markup=low_keyboard.low_markup_dict)


@bot.message_handler(commands=['custom'])
def send_high(message: Message) -> None:
    bot.send_message(message.chat.id, 'Нажми на кнопку и выбери подборку, которую ты хочешь получить! 👇',
                     reply_markup=custom_keyboard.custom_markup)
    bot.set_state(message.from_user.id, States.custom_type, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['state'] = States.custom_type


@bot.message_handler(state=States.custom_type)
def state_low(message: Message) -> None:
    go_to_count(message=message, sort_type=-1, markup=custom_keyboard.custom_markup_dict)


@bot.message_handler(state=States.count)
def state_count(message: Message) -> None:
    check_text = message.text
    if check_text.isdigit() and 1 <= int(check_text) <= 10:
        film_limit = int(check_text)
    else:
        bot.reply_to(message, 'Похоже ты ввел неверное число! Введи число от 1 до 10')
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        from_markup = film_data.get('from_markup')
        sort_type = film_data.get('sort_type')
        markup = film_data.get('markup')
        state = film_data.get('state')
    get_films(message=message, sort_type=sort_type, limit=film_limit, sort_field=markup.get(from_markup))
    bot.set_state(message.from_user.id, state, message.chat.id)


@bot.message_handler(func=lambda message: True)
def greetings(message: Message) -> None:
    user_name = message.from_user.first_name
    bot.send_chat_action(chat_id=message.chat.id,
                         action='typing')
    bot.reply_to(message,
                 '{name}, для работы выбери доступную команду из меню или введи команду '
                 '/help, чтобы узнать больше о моих возможностях.'.format(name=user_name))
