from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    """
    Классы:
    - StatesGroup: Базовый класс для группы состояний.
    - State: Класс, представляющий отдельное состояние.

    Объекты:
    - base: Объект состояния для базового состояния.
    - value_range: Объект состояния для состояния ввода пользовательского диапазона.
    - req_state: Объект состояния для состояния запроса подборок фильмов.
    - count: Объект состояния для состояния ввода количества фильмов в запросе.

    """

    base = State()
    value_range = State()
    req_state = State()
    count = State()
