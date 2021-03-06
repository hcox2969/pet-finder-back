import os
from peewee import *
import datetime
from flask_login import UserMixin
from playhouse.db_url import connect


if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))

else:
    DATABASE = SqliteDatabase('pets.sqlite')

class User(UserMixin, Model):
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()
    phone=CharField()

    class Meta:
        database = DATABASE



class Pet(Model):
    petName = CharField()
    aboutPet=CharField()
    dateLost=DateTimeField(default=datetime.datetime.now)
    reunited=BooleanField(default=False)
    user=ForeignKeyField(User, backref='pets')
    photo=CharField()
    status=CharField()
    zipCode=CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Pet], safe=True)
    print("TABLES Created")
    DATABASE.close()
