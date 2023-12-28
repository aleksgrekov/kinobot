from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=['help'])
def send_help(message: Message):
    command_list = ['/{} - {}'.format(command, desk) for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, '\n'.join(command_list))
