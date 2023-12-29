from telebot.types import Message

from loader import bot


@bot.message_handler(func=lambda message: True)
def greetings(message: Message):
    user_name = message.from_user.first_name
    bot.reply_to(message,
                 '{name}, для работы выбери доступную команду из меню или введи команду '
                 '/help, чтобы узнать больше о моих возможностях.'.format(name=user_name))
