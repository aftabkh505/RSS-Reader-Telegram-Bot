from peewee import *
from . import Configs

# Instance of the database (MySQL)
db = MySQLDatabase(Configs.DB.NAME, **{'host': Configs.DB.HOST, 'port': Configs.DB.PORT, 'user': Configs.DB.USER})


# Base model for all models
class BaseModel(Model):
    class Meta:
        database = db


# Bot clients model
class Client(BaseModel):
    chat_id = CharField(unique=True)
    last_checked_time = DateTimeField()
    is_registered = BooleanField()

    class Meta:
        table_name = Configs.DB.CLIENTS_TABLE
