from peewee import *

db = SqliteDatabase('nl_3.db')


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
    address = CharField(null=True)
    telephone = CharField(12)
    responsible_id = CharField()
    photo = BlobField(null=True)
    photo_path = CharField(null=True)

    class Meta:
        db_table = 'users'


class Loyality(BaseModel):
    name = CharField()

    class Meta():
        db_table = 'loyalitys'


class Storonnik(BaseModel):
    l_name = CharField(30)
    name = CharField(30)
    age = IntegerField(3)
    address = CharField(null=True)
    telephone = CharField(12)
    social_media = CharField(null=True)
    responsible = ForeignKeyField(User)
    loyality = ForeignKeyField(Loyality)
    desc = CharField(null=True)

    class Meta:
        db_table = 'storonniks'


class E_type(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'e_types'


class Event(BaseModel):
    e_type = ForeignKeyField(E_type)
    name = CharField()
    budget = IntegerField(null=True)
    responsible = ForeignKeyField(User)
    desc = TextField(null=True)

    class Meta:
        db_table = 'events'


class Action(BaseModel):
    event = ForeignKeyField(Event)
    storonnik = ForeignKeyField(Storonnik)
    address = CharField(null=True)
    date = DateTimeField(null=True)
    desc = TextField(null=True)

    class Meta:
        db_table = 'actions'


class Kpi(BaseModel):
    name = CharField()
    count = IntegerField()
    deadline = DateTimeField(null=True)
    obj = ForeignKeyField(User)
    desc = TextField(null=True)

    class Meta:
        db_table = 'kpis'


class Quote(BaseModel):
    text = TextField()

    class Meta:
        db_table = 'quotes'
