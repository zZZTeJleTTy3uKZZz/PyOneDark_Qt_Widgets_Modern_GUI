from peewee import *

db = SqliteDatabase('nl.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Role(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'roles'


class User(BaseModel):
    role = ForeignKeyField(Role)
    login = CharField()
    passwd = CharField()
    l_name = CharField(30)
    name = CharField(30)
    age = IntegerField(3)
    address = CharField()
    telephone = CharField(12)
    responsible_id = CharField()
    photo = BlobField()
    photo_path = CharField()

    class Meta:
        db_table = 'users'


class Storonnik(BaseModel):
    l_name = CharField(30)
    name = CharField(30)
    age = IntegerField(3)
    address = CharField()
    telephone = CharField(12)
    social_media = CharField()
    responsible = ForeignKeyField(User)
    desc = CharField()

    class Meta:
        db_table = 'storonniks'


class E_type(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'e_types'


class Event(BaseModel):
    e_type = ForeignKeyField(E_type)
    name = CharField()
    budget = IntegerField()
    responsible = ForeignKeyField(User)
    desc = TextField()

    class Meta:
        db_table = 'events'


class Action(BaseModel):
    event = ForeignKeyField(Event)
    storonnik = ForeignKeyField(Storonnik)
    address = CharField()
    date = DateTimeField()
    desc = TextField()

    class Meta:
        db_table = 'actions'


class Task(BaseModel):
    name = CharField()
    deadline = DateTimeField()
    owner = ForeignKeyField(User)
    obj = ForeignKeyField(User)
    desc = TextField()

    class Meta:
        db_table = 'tasks'


class Kpi_type(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'kpi_types'

class Kpi(BaseModel):
    name = CharField()
    type_ = ForeignKeyField(Kpi_type)
    count = IntegerField()
    deadline = DateTimeField()
    obj = ForeignKeyField(User)
    desc = TextField()

    class Meta:
        db_table = 'kpis'

class Quote(BaseModel):
    text = TextField()

    class Meta:
        db_table = 'quotes'