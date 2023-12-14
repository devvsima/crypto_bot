from peewee import *

db = SqliteDatabase('database/database.sqlite')

class Person(Model):
    id = IntegerField(primary_key=True)
    # birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

Person.create_table()


def newUsr(id):
    newUsr = Person.create(id=id, is_relative=True)
    