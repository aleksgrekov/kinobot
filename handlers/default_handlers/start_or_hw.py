from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['start', 'hello_world'])
def send_welcome(message: Message):
    bot.reply_to(message, "Привет! В этом боте вы сможете получить различные подборки фильмов сайта \"Кинопоиск\"")
