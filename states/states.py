from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    base = State()
    high_type = State()
    low_type = State()
    custom_type = State()
    value_range = State()
    count = State()
