from peewee import (SqliteDatabase, Model, CharField,
                    AutoField, ForeignKeyField, IntegerField)
from config_data.config import DB_PATH

db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class BotRequest(BaseModel):
    req_id = AutoField()
    user_id = ForeignKeyField(User, backref='history')
    command = CharField()
    req_date = CharField()
    period = CharField(null=True)
    count = CharField()

    def __str__(self):
        result = f'{self.req_date}\nЗапрос: {self.command} '
        if self.period:
            result += f'\nПериод: {self.period}'
        result += f'\nКоличество фильмов: {self.count}\n'
        return result


def create_models():
    db.create_tables(BaseModel.__subclasses__())
