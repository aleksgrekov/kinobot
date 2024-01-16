from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    base = State()
    value_range = State()
    req_state = State()
    count = State()
