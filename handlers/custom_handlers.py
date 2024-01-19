from typing import List
from datetime import date
from telebot.types import Message

from loader import bot
from states.states import States
from config_data.config import DATE_FORMAT
from database.models import User, BotRequest
from handlers.function import check_registration, get_films
from keyboards import high_keyboard, low_keyboard, custom_keyboard


@bot.message_handler(state='*', commands=['high'])
def send_high(message: Message) -> None:
    """
    Обработчик команды /high для запроса подборок с высоким рейтингом или длительностью.

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    if not check_registration(message=message):
        return
    bot.send_message(message.chat.id, 'Нажми на кнопку и выбери подборку, '
                                      'которую ты хочешь получить! 👇',
                     reply_markup=high_keyboard.high_markup)
    bot.set_state(message.from_user.id, States.req_state, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['state'] = 'high_type'
        film_data['req_history'] = {'user_id': message.from_user.id}


@bot.message_handler(state='*', commands=['low'])
def send_low(message: Message) -> None:
    """
    Обработчик команды /low для запроса подборок с низким возрастным рейтингом,
    самых старых или самых коротких фильмов.

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    if not check_registration(message=message):
        return
    bot.send_message(message.chat.id, 'Нажми на кнопку и выбери подборку, '
                                      'которую ты хочешь получить! 👇',
                     reply_markup=low_keyboard.low_markup)
    bot.set_state(message.from_user.id, States.req_state, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['state'] = 'low_type'
        film_data['req_history'] = {'user_id': message.from_user.id}


@bot.message_handler(state='*', commands=['custom'])
def send_custom(message: Message) -> None:
    """
    Обработчик команды /custom для запроса подборок с пользовательскими параметрами.

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    if not check_registration(message=message):
        return
    bot.send_message(message.chat.id, 'Нажми на кнопку и выбери подборку, '
                                      'которую ты хочешь получить! 👇',
                     reply_markup=custom_keyboard.custom_markup)
    bot.set_state(message.from_user.id, States.value_range, message.chat.id)


@bot.message_handler(state="*", commands=['history'])
def get_history(message: Message) -> None:
    """
    Обработчик команды /history для получения истории запросов пользователя.

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return
    history: List[BotRequest] = user.history.order_by(-BotRequest.req_date, -BotRequest.req_id).limit(10)

    result = []
    result.extend(map(str, reversed(history)))

    if not result:
        bot.send_message(message.from_user.id, "У вас ещё нет задач")
        return

    bot.send_message(message.from_user.id, "\n".join(result))
    bot.set_state(message.from_user.id, States.base)


@bot.message_handler(state=States.value_range)
def input_range(message: Message) -> None:
    """
    Обработчик ввода пользовательского диапазона для команды /custom

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    if message.text == custom_keyboard.item1.text:
        bot.reply_to(message, 'Введи год выхода фильма (формат ввода: 2020) '
                              'или период (формат ввода: 1874-2050).')
    elif message.text == custom_keyboard.item2.text:
        bot.reply_to(message, 'Введи диапазон рейтинг фильма (формат ввода: 7) '
                              'или диапазон (формат ввода: 5-10)')
    else:
        bot.reply_to(message,
                     'Не нужно самодеятельности!😁 '
                     'Нажми на кнопку и выбери подборку, которую ты хочешь получить! 👇')
        return
    bot.set_state(message.from_user.id, States.req_state, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['req_history'] = {'user_id': message.from_user.id}
        film_data['req_history']['command'] = message.text
        film_data['state'] = 'custom_type'


@bot.message_handler(state=States.req_state)
def req_state(message: Message) -> None:
    """
    Обработчик запроса подборок для команд (/high, /low, /custom)

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['req_history']['req_date'] = date.today().strftime(DATE_FORMAT)
        film_data['sort_type'] = -1

        if film_data.get('state') != 'custom_type':
            if film_data.get('state') == 'high_type':
                film_data['markup'] = high_keyboard.high_markup_dict
            elif film_data.get('state') == 'low_type':
                film_data['sort_type'] = 1
                film_data['markup'] = low_keyboard.low_markup_dict

            if message.text not in film_data.get('markup'):
                bot.reply_to(message,
                             'Не нужно самодеятельности!😁 '
                             'Нажми на кнопку и выбери подборку, '
                             'которую ты хочешь получить! 👇')
                return
            film_data['req_history']['command'] = message.text
        else:
            film_data['req_history']['period'] = message.text
            film_data['markup'] = custom_keyboard.custom_markup_dict

        bot.reply_to(message, 'Из скольки фильмов ты будешь выбирать? '
                              'Введи число от 1 до 10')
        bot.set_state(message.from_user.id, States.count, message.chat.id)


@bot.message_handler(state=States.count)
def state_count(message: Message) -> None:
    """
    Обработчик ввода количества фильмов для запроса.

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    check_text = message.text
    if check_text.isdigit() and 1 <= int(check_text) <= 10:
        film_limit = int(check_text)
    else:
        bot.reply_to(message, 'Похоже ты ввел неверное число! Введи число от 1 до 10')
        return
    with bot.retrieve_data(message.from_user.id, message.chat.id) as film_data:
        film_data['req_history']['count'] = film_limit
        from_markup = film_data['req_history'].get('command')
        sort_type = film_data.get('sort_type')
        markup = film_data.get('markup')
        state = film_data.get('state')
        range_value = film_data['req_history'].get('period')
    new_database_entry = BotRequest(**film_data['req_history'])
    new_database_entry.save()
    get_films(message=message,
              sort_type=sort_type,
              limit=film_limit,
              sort_field=markup.get(from_markup),
              range_value=range_value)

    set_state = States.base
    if state == 'high_type':
        set_state = States.req_state
    elif state == 'low_type':
        set_state = States.req_state
    elif state == 'custom_type':
        set_state = States.value_range
    bot.set_state(message.from_user.id, set_state, message.chat.id)


@bot.message_handler(func=lambda message: True)
def other_message(message: Message) -> None:
    """
    Обработчик сторонних сообщений пользователя.

    :param: message: Объект сообщения от пользователя.
    :type: Message

    """

    user_name = message.from_user.first_name
    bot.send_chat_action(chat_id=message.chat.id,
                         action='typing')
    bot.reply_to(message,
                 '{name}, для работы выбери доступную команду из меню или введи команду '
                 '/help, чтобы узнать больше о моих возможностях.'.format(name=user_name))
