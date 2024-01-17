from peewee import (SqliteDatabase, Model, CharField,
                    AutoField, ForeignKeyField, IntegerField)
from config_data.config import DB_PATH

db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    """
    Базовый класс модели данных для использования базы данных Peewee.

    Атрибуты:
    - Meta: Подкласс, определяющий базу данных для модели.

    """

    class Meta:
        database = db


class User(BaseModel):
    """
    Модель данных для представления пользователя бота.

    Атрибуты:
    - user_id: Идентификатор пользователя (первичный ключ).
    - username: Логин пользователя.
    - first_name: Имя пользователя.
    - last_name: Фамилия пользователя (может быть None).

    """

    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class BotRequest(BaseModel):
    """
    Модель данных для представления истории запросов пользователей.

    Атрибуты:
    - req_id: Идентификатор запроса (автоинкрементируемый).
    - user_id: Идентификатор пользователя (внешний ключ, связан с User).
    - command: Команда, отправленная пользователем.
    - req_date: Дата и время запроса в формате строки.
    - period: Период запроса (может быть None).
    - count: Количество фильмов в запросе.

    """

    req_id = AutoField()
    user_id = ForeignKeyField(User, backref='history')
    command = CharField()
    req_date = CharField()
    period = CharField(null=True)
    count = CharField()

    def __str__(self):
        """
        Строковое представление объекта BotRequest.

        :return: Строковое представление объекта BotRequest.
        :rtype: str
        """

        result = f'{self.req_date}\nЗапрос: {self.command} '
        if self.period:
            result += f'\nПериод: {self.period}'
        result += f'\nКоличество фильмов: {self.count}\n'
        return result


def create_models():
    """
    Функция для создания таблиц в базе данных для всех подклассов BaseModel.

    """

    db.create_tables(BaseModel.__subclasses__())
