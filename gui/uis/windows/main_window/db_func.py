from qt_core import *
from models import *
import os
import sys

class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return

def errors_sel():
    msg = QMessageBox()
    msg.setWindowTitle('Ошибка')
    msg.setText('Выберите строку')
    msg.setIcon(QMessageBox.Warning)
    x = msg.exec_()


def loadcollum(row, t, *func):
    for i in range(len(func)):
        t.setItem(row, i, QTableWidgetItem(func[i]))
    

def deltable(table):
    for row in range(table.rowCount()):
        table.removeRow(0)
    for col in range(table.columnCount()):
        table.removeColumn(0)
    


def colum_header(table, list_header):
    
    table.setColumnCount(len(list_header))
    for i in range(len(list_header)):
        delegate = ReadOnlyDelegate(table)
        table.setItemDelegateForColumn(i, delegate)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setSelectionMode(QAbstractItemView.ExtendedSelection)
    # table.ItemIsEditable(False)
    
    # table.setSelectionBehavior(QAbstractItemView.SelectRows)
    table.setHorizontalHeaderLabels(list_header)
    table.setColumnHidden(len(list_header)-1, True)

    if list_header[0] == "Фото":
         table.setColumnHidden(len(list_header)-2, True)
   

def show_image(id_user=None, width=300):
    if id_user != None:
        ph = User.select().where(User.id == id_user)
        for p in ph:
            img = p.photo
            ext = p.photo_path[p.photo_path.rfind('.'):len(p.photo_path)]

    pixmap = QPixmap()

    pixmap.loadFromData(img, ext)
    pixmap_resize = pixmap.scaled(130, width, Qt.KeepAspectRatio)
    return pixmap_resize


def getImageLable(image, idp):
    il = QLabel()
    il.setText("")
    try:
        il.setPixmap(show_image(idp))
    except:
        il.setText("Нет фото")
    return il

        

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
                if u == 0:
                    item = getImageLable(users[u], users[len(users)-1])
                    table.setCellWidget(row, u, item)
                else:
                    table.setItem(row, u, QTableWidgetItem(users[u]))
                    table.setRowHeight(row, 150)
            row += 1

    if target_name == 'Role':
        row = 0
        for val in value:
            roles = [val.name, val.id]
        for u in range(len(roles)):
            table.setItem(row, u, QTableWidgetItem(roles[u]))
            table.setRowHeight(row, 30)
        row += 1


    if target_name == 'Storonnik':
        row = 0
        for val in value:
            storonniks = [val.l_name, val.name, str(val.age), val.address, val.telephone, val.social_media, f"{val.responsible.l_name} {val.responsible.name}", 
            val.loyality.name, str(len(Action.select().where(Action.storonnik_id == val.id))), val.desc, str(val.id)]
            for u in range(len(storonniks)):
                table.setItem(row, u, QTableWidgetItem(storonniks[u]))
                table.setRowHeight(row, 30)
            row += 1

    if target_name == "Event":
        row = 0
        for val in value:
            events = [val.e_type.name, val.name, str(val.budget), 
                f"{val.responsible.l_name} {val.responsible.name}", 
                str(len(Action.select().where(Action.event_id == val.id))), val.desc, str(val.id)]
            for u in range(len(events)):
                table.setItem(row, u, QTableWidgetItem(events[u]))
                table.setRowHeight(row, 30)
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