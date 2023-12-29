from peewee import SqliteDatabase, Model, CharField, IntegerField
from config_data.config import DB_PATH
import os

db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


def create_models():
    db.create_tables(BaseModel.__subclasses__())
