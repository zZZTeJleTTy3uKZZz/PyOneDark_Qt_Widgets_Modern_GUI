from models import *


def create_role():
    # Роли в структуре
    roles = [
        {'name':'Администратор'},
        {'name':'Секретарь РО'},
        {'name':'Бригадир'},
        {'name':'Кандидат'}
    ]

    Role.insert_many(roles).execute()

def create_user():
    rolesid = Role.select()
    users = [
        {'role_id':rolesid[0], 'l_name':'Тест', 'name':'Тестович', 'login':'1', 'passwd':'1', 'age':19, 'address':'ул. Бруснева, д.12', 'telephone':'+79288201158', 'responsible_id' : 1},
        {'role_id':rolesid[0], 'l_name':'Семенов', 'name':'Дмитрий', 'login':'admin', 'passwd':'admin123BOG', 'age':19, 'address':'ул. Бруснева, д.12', 'telephone':'+79288201158', 'responsible_id' : 1},
        {'role_id':rolesid[1], 'l_name':'Исупов', 'name':'Иван', 'login':'i.isupov', 'passwd':'pass12udy1', 'age':24, 'address':'Ставропольский край', 'telephone':'+78005553535', 'responsible_id' : 1},
        {'role_id':rolesid[2], 'l_name':'Сизякина', 'name':'Виктория', 'login':'v.sizyakina', 'passwd':'bestgirlforever', 'age':19, 'address':'ул. Ставропольская, д. 13', 'telephone':'+799128ve980', 'responsible_id' : 3},
        {'role_id':rolesid[2], 'l_name':'Иванов', 'name':'Владимир', 'login':'v.ivanov', 'passwd':'12ioh8doh1', 'age':20, 'address':'ул. 50 лет ВЛКСМ, д. 55', 'telephone':'+79562543381', 'responsible_id' : 3},
        {'role_id':rolesid[2], 'l_name':'Финансов', 'name':'Министр', 'login':'m.finansov', 'passwd':'EtoNastoysheeImya', 'age':666, 'address':'ул. Первомайская, д.64', 'telephone':'+79862731584', 'responsible_id' : 3},
        {'role_id':rolesid[2], 'l_name':'Денисов', 'name':'Игорь', 'login':'i.denisov', 'passwd':'ProstoDED2021', 'age':34, 'address':'ул. В самое сердечко, д. 1', 'telephone':'+79280006688', 'responsible_id' : 3},
        {'role_id':rolesid[2], 'l_name':'Комаров', 'name':'Анатолий', 'login':'a.komarov', 'passwd':'qopwjd81jds81H', 'age':54, 'address':'ул. Симметричная, д.182', 'telephone':'+79654705834', 'responsible_id' : 3},
        {'role_id':rolesid[3], 'l_name':'Степанян', 'name':'Ваган', 'login':'v.stepanyan', 'passwd':'EasterEgg', 'age':22, 'address':'Москва', 'telephone':'+82695730656', 'responsible_id' : 6},
        {'role_id':rolesid[3], 'l_name':'Первышев', 'name':'Роман', 'login':'r.pervishev', 'passwd':'JlirA_PyK0}|[0TT0B', 'age':18, 'address':'ул. Мира, д.212', 'telephone':'+72680390000', 'responsible_id' : 4},
        {'role_id':rolesid[3], 'l_name':'Самохин', 'name':'Александр', 'login':'a.samohin', 'passwd':'Bro', 'age':27, 'address':'ул. ГТО, д.999', 'telephone':'+77777777777', 'responsible_id' : 5}
    ]

    User.insert_many(users).execute()


def create_loyality():
    loyality = [
        {'name':'1 касание'},
        {'name':'1 мероприятие'},
        {'name':'Поддерживает'},
        {'name':'Активничает'},
        {'name':'Придёт голосовать'}
    ]

    Loyality.insert_many(loyality).execute()


def create_storonnik():
    usersid = User.select()
    loyalityid = Loyality.select()
    storonniks = [
        {'responsible_id':usersid[3], 'loyality_id':loyalityid[0], 'l_name':'Сидоров', 'name':'Инокентий', 'age':25, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/lolel182'},
        {'responsible_id':usersid[5], 'loyality_id':loyalityid[3], 'l_name':'Катинов', 'name':'Павел', 'age':22, 'address':'ул. Спартака, д.229', 'telephone':'+79716306488', 'social_media':'vk.com/lolel182'},
        {'responsible_id':usersid[6], 'loyality_id':loyalityid[2], 'l_name':'Кузинков', 'name':'Никита', 'age':26, 'address':'ул. Мира, д.18', 'telephone':'+79716306488', 'social_media':'vk.com/lolel182'},
        {'responsible_id':usersid[7], 'loyality_id':loyalityid[2], 'l_name':'Волубев', 'name':'Георгий', 'age':28, 'address':'ул. Тухачевского, д.46', 'telephone':'+79716306488', 'social_media':'vk.com/lxj1jds93'},
        {'responsible_id':usersid[7], 'loyality_id':loyalityid[4], 'l_name':'Руснак', 'name':'Степан', 'age':20, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/somcu18c'},
        {'responsible_id':usersid[3], 'loyality_id':loyalityid[3], 'l_name':'Хромов', 'name':'Даниил', 'age':21, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/lolel182'},
        {'responsible_id':usersid[3], 'loyality_id':loyalityid[1], 'l_name':'Пермякова', 'name':'Светлана', 'age':19, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/lolel182'},
        {'responsible_id':usersid[4], 'loyality_id':loyalityid[1], 'l_name':'Гаценко', 'name':'Леонид', 'age':25, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/chi1oc81'},
        {'responsible_id':usersid[3], 'loyality_id':loyalityid[0], 'l_name':'Мельников', 'name':'Максим', 'age':24, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/s1px18xh'},
        {'responsible_id':usersid[6], 'loyality_id':loyalityid[1], 'l_name':'Турышева', 'name':'Анастасия', 'age':29, 'address':'ул. Мимоз, д.4', 'telephone':'+79761306488', 'social_media':'vk.com/lolel182'},
        {'responsible_id':usersid[3], 'loyality_id':loyalityid[4], 'l_name':'Кудряшова', 'name':'Инесса', 'age':42, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/vsod83f'},
        {'responsible_id':usersid[6], 'loyality_id':loyalityid[4], 'l_name':'Лапина', 'name':'Алла', 'age':23, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/15lolel182'},
        {'responsible_id':usersid[3], 'loyality_id':loyalityid[2], 'l_name':'Никишина', 'name':'Инна', 'age':25, 'address':'ул. Мимоз, д.4', 'telephone':'+79719206488', 'social_media':'vk.com/19hct2nx'},
        {'responsible_id':usersid[8], 'loyality_id':loyalityid[2], 'l_name':'Бочкарёва', 'name':'Вера', 'age':21, 'address':'ул. Мимоз, д.4', 'telephone':'+79716306488', 'social_media':'vk.com/lolel182'},
    ]
    Storonnik.insert_many(storonniks).execute()


def create_e_types():
    e_types = [
        {'name':'Акция'},
        {'name':'Мероприятие'},
        {'name':'Социальный опрос'},
        {'name':'Интенсив'},
        {'name':'Интервью'},
        {'name':'Обращение'},
        {'name':'Ответы на вопросы'},
        {'name':'Встреча'},
        {'name':'Перфоманс'}
    ]

    E_type.insert_many(e_types).execute()


def create_events():
    usersid = User.select()
    e_typesid = E_type.select()
    events = [
        {'e_type_id':e_typesid[8], 'name':'Создание CRM', 'budget':0, 'responsible':usersid[8], 'desc':'Разработка CRM Системы и успешная сдача курсового проекта'},
        {'e_type_id':e_typesid[0], 'name':'Выгул собак', 'budget':1000, 'responsible':usersid[9], 'desc':'Какое-то описание'},
        {'e_type_id':e_typesid[1], 'name':'Чаепитие', 'budget':500, 'responsible':usersid[9], 'desc':'Какое-то описание'},
        {'e_type_id':e_typesid[5], 'name':'Замена пандуса', 'budget':1200, 'responsible':usersid[10], 'desc':'Какое-то описание'},
        {'e_type_id':e_typesid[2], 'name':'Хватает ли МРОТ для выживания', 'budget':5000, 'responsible':usersid[8], 'desc':'Какое-то описание'},
        {'e_type_id':e_typesid[2], 'name':'Позвони родителям', 'budget':4000, 'responsible':usersid[8], 'desc':'Как часто вы говорите своим родителям слова любви и благодарности'},
        {'e_type_id':e_typesid[7], 'name':'Ликвидация маршруток', 'budget':50, 'responsible':usersid[10], 'desc':'Какое-то описание'},
        {'e_type_id':e_typesid[0], 'name':'Раздача ёлочных шаров', 'budget':200000, 'responsible':usersid[8], 'desc':'Какое-то описание'},
        {'e_type_id':e_typesid[1], 'name':'МК - как стать активистом партии «Новые люди»', 'budget':1000, 'responsible':usersid[10], 'desc':''},
        {'e_type_id':e_typesid[3], 'name':'Интенсив №1', 'budget':30000, 'responsible':usersid[9], 'desc':''},
        {'e_type_id':e_typesid[6], 'name':'Ликбез', 'budget':2000, 'responsible':usersid[8], 'desc':'Меньше знаешь - крепче спишь'},
     ]

    Event.insert_many(events).execute()

with db:
    # db.create_tables([Role, User, Storonnik, E_type, Event, Action, Kpi, Quote, Loyality])
    # create_role()
    # create_user()
    # create_loyality()
    # create_storonnik()
    create_e_types()
    create_events()
