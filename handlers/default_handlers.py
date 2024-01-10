from peewee import IntegrityError
from telebot.types import Message

from loader import bot
from states.states import States
from database.models import User
from config_data.config import DEFAULT_COMMANDS


@bot.message_handler(commands=['start'])
def handler_start(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    bot.set_state(message.from_user.id, States.base, message.chat.id)
    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message,
                     'Привет, {name}! Я - бот, который поможет тебе определиться с фильмом на '
                     'вечер. Для начала работы выбери доступную команду из меню или введи '
                     'команду /help, чтобы узнать больше о моих возможностях.'.format(name=first_name))
    except IntegrityError:
        bot.reply_to(message, 'И снова здравствуйте, {name}!'.format(name=first_name))


@bot.message_handler(commands=['help'])
def send_help(message: Message) -> None:
    command_list = ['/{} - {}'.format(command, desk) for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, '\n'.join(command_list))
    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(state="*", commands=['cancel'])
def any_state(message):
    bot.send_message(message.chat.id, "До свидания!")
    bot.delete_state(message.from_user.id, message.chat.id)
