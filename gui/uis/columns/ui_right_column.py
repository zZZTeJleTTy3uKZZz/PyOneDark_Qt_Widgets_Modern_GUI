# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_column.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(218, 834)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.users_menu = QWidget()
        self.users_menu.setObjectName(u"users_menu")
        self.verticalLayout = QVBoxLayout(self.users_menu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_1 = QLabel(self.users_menu)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(16777215, 167777))
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.l_name = QWidget(self.users_menu)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setMinimumSize(QSize(0, 50))
        self.l_name.setMaximumSize(QSize(16777215, 50))
        self.l_name__l = QHBoxLayout(self.l_name)
        self.l_name__l.setObjectName(u"l_name__l")

        self.verticalLayout.addWidget(self.l_name)

        self.name = QWidget(self.users_menu)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 50))
        self.name.setMaximumSize(QSize(16777215, 50))
        self.name__l = QHBoxLayout(self.name)
        self.name__l.setObjectName(u"name__l")

        self.verticalLayout.addWidget(self.name)

        self.table_role = QWidget(self.users_menu)
        self.table_role.setObjectName(u"table_role")
        self.table_role.setMinimumSize(QSize(0, 50))
        self.table_role.setMaximumSize(QSize(16777215, 50))
        self.table_role__l = QHBoxLayout(self.table_role)
        self.table_role__l.setObjectName(u"table_role__l")

        self.verticalLayout.addWidget(self.table_role)

        self.login = QWidget(self.users_menu)
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(0, 50))
        self.login.setMaximumSize(QSize(16777215, 50))
        self.login__l = QHBoxLayout(self.login)
        self.login__l.setObjectName(u"login__l")

        self.verticalLayout.addWidget(self.login)

        self.passwd = QWidget(self.users_menu)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setMinimumSize(QSize(0, 50))
        self.passwd.setMaximumSize(QSize(16777215, 50))
        self.passwd__l = QHBoxLayout(self.passwd)
        self.passwd__l.setObjectName(u"passwd__l")

        self.verticalLayout.addWidget(self.passwd)

        self.age = QWidget(self.users_menu)
        self.age.setObjectName(u"age")
        self.age.setMinimumSize(QSize(0, 50))
        self.age.setMaximumSize(QSize(16777215, 50))
        self.age__l = QHBoxLayout(self.age)
        self.age__l.setObjectName(u"age__l")

        self.verticalLayout.addWidget(self.age)

        self.address = QWidget(self.users_menu)
        self.address.setObjectName(u"address")
        self.address.setMinimumSize(QSize(0, 50))
        self.address.setMaximumSize(QSize(16777215, 50))
        self.address__l = QHBoxLayout(self.address)
        self.address__l.setObjectName(u"address__l")

        self.verticalLayout.addWidget(self.address)

        self.telephone = QWidget(self.users_menu)
        self.telephone.setObjectName(u"telephone")
        self.telephone.setMinimumSize(QSize(0, 50))
        self.telephone.setMaximumSize(QSize(16777215, 50))
        self.telephone__l = QHBoxLayout(self.telephone)
        self.telephone__l.setObjectName(u"telephone__l")

        self.verticalLayout.addWidget(self.telephone)

        self.responsible = QWidget(self.users_menu)
        self.responsible.setObjectName(u"responsible")
        self.responsible.setMinimumSize(QSize(0, 50))
        self.responsible.setMaximumSize(QSize(16777215, 50))
        self.responsible__l = QHBoxLayout(self.responsible)
        self.responsible__l.setObjectName(u"responsible__l")

        self.verticalLayout.addWidget(self.responsible)

        self.photo = QWidget(self.users_menu)
        self.photo.setObjectName(u"photo")
        self.photo.setMinimumSize(QSize(0, 50))
        self.photo.setMaximumSize(QSize(16777215, 50))
        self.photo__l = QHBoxLayout(self.photo)
        self.photo__l.setObjectName(u"photo__l")

        self.verticalLayout.addWidget(self.photo)

        self.save = QWidget(self.users_menu)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(0, 50))
        self.save.setMaximumSize(QSize(16777215, 50))
        self.save__l = QHBoxLayout(self.save)
        self.save__l.setObjectName(u"save__l")

        self.verticalLayout.addWidget(self.save)

        self.menus.addWidget(self.users_menu)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("RightColumn", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Menu 2 - Right Menu", None))
    # retranslateUi

