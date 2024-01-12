from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    base = State()
    high_type = State()
    low_type = State()
    count = State()
