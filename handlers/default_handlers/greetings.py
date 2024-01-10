from telebot.types import Message

from loader import bot


@bot.message_handler(func=lambda message: True)
def greetings(message: Message):
    bot.reply_to(message, 'Привет! Напиши /start, /help или /hello_world для того, чтобы я рассказал о себе!')
