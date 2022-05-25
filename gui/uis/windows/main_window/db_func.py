from models import *
from qt_core import *

def errors_sel():
    msg = QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText('Выберите строку')
    msg.setIcon(QMessageBox.Warning)
    x = msg.exec_()


def loadcollum(row, t, *func):
    for i in range(len(func)):
        t.setItem(row, i, QTableWidgetItem(func[i]))
    
    
def colum_header(table, list_header):
    table.setColumnCount(len(list_header))
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setSelectionMode(QAbstractItemView.ExtendedSelection)
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    table.setHorizontalHeaderLabels(list_header)
    table.setColumnHidden(len(list_header)-1, True)

    if list_header[0] == "Фото":
         table.setColumnHidden(len(list_header)-2, True)
   

        

def load_rows(table, target, target_name):
    value = target.select()
    table.setRowCount(len(value))

    #Польщователи
    if target_name == 'User':
        row = 0
        for val in value:
            res = User.select().where(User.id == val.responsible_id)
            for r in res:
                users = [str(val.photo), val.l_name, val.name, val.role.name, val.login, val.passwd, str(val.age), val.address, val.telephone, str(f"{r.l_name} {r.name}"), str(val.photo_path), str(val.id)]
            for u in range(len(users)):
                table.setItem(row, u, QTableWidgetItem(users[u]))
                table.setRowHeight(row, 150)
            row += 1
            


def loaddata(table, t, types):
    value = table.select()

    if types == 'Brigada':
        value = table.select().where(User.role_id == 2)
    t.setRowCount(len(value))
    tablerow = 0

    if types == 'Event':
        for val in value:
            zn = [val.e_type.name, val.name, str(val.budget), 
                f"{val.responsible.l_name} {val.responsible.name}", 
                str(len(Action.select().where(Action.event_id == val.id))), val.desc, str(val.id)]
            loadcollum(tablerow, t, *zn)
            tablerow += 1

    if types == 'Storonnik':
        for val in value:
            zn = [val.l_name, val.name, str(val.age), val.address, val.telephone, val.social_media, f"{val.brigadir.l_name} {val.brigadir.name}", str(
                len(Action.select().where(Action.active_id == val.id))), str(val.id)]
            loadcollum(tablerow, t, *zn)
            tablerow += 1

    if types == 'Brigada':
        for val in value:
            zn = [val.l_name, val.name, val.login, val.passwd, str(val.age), val.address, val.telephone, str(
                len(Storonnik.select().where(Storonnik.brigadir_id == val.id))), str(
                len(Event.select().where(Event.responsible_id == val.id))), str(val.id)]
            loadcollum(tablerow, t, *zn)
            tablerow += 1