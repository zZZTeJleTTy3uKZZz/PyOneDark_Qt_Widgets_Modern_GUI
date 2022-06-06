# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_column.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        themes = Themes()
        self.themes = themes.items
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(218, 878)
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
        self.scrollArea = PyScrollArea(self.users_menu,
        border_size=2,
        color=self.themes["app_color"]["text_foreground"],
        bg_color=self.themes["app_color"]["bg_two"],
        bg_color_hover=self.themes["app_color"]["dark_three"],
        bg_color_pressed=self.themes["app_color"]["dark_three"],
        context_color=self.themes["app_color"]["context_color"],
        scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
        scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        )
        self.scrollArea.setObjectName(u"scrollArea")

        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 858))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.name_2 = QLabel(self.scrollAreaWidgetContents)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setMinimumSize(QSize(0, 30))
        self.name_2.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(16)
        self.name_2.setFont(font)
        self.name_2.setStyleSheet(u"font-size: 16pt")
        self.name_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.name_2)

        self.l_name = QWidget(self.scrollAreaWidgetContents)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setMinimumSize(QSize(0, 50))
        self.l_name.setMaximumSize(QSize(16777215, 50))
        self.l_name__l = QHBoxLayout(self.l_name)
        self.l_name__l.setObjectName(u"l_name__l")

        self.verticalLayout_3.addWidget(self.l_name)

        self.name = QWidget(self.scrollAreaWidgetContents)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 50))
        self.name.setMaximumSize(QSize(16777215, 50))
        self.name__l = QHBoxLayout(self.name)
        self.name__l.setObjectName(u"name__l")

        self.verticalLayout_3.addWidget(self.name)

        self.table_role = QWidget(self.scrollAreaWidgetContents)
        self.table_role.setObjectName(u"table_role")
        self.table_role.setMinimumSize(QSize(0, 50))
        self.table_role.setMaximumSize(QSize(16777215, 50))
        self.table_role__l = QHBoxLayout(self.table_role)
        self.table_role__l.setObjectName(u"table_role__l")

        self.verticalLayout_3.addWidget(self.table_role)

        self.login = QWidget(self.scrollAreaWidgetContents)
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(0, 50))
        self.login.setMaximumSize(QSize(16777215, 50))
        self.login__l = QHBoxLayout(self.login)
        self.login__l.setObjectName(u"login__l")

        self.verticalLayout_3.addWidget(self.login)

        self.passwd = QWidget(self.scrollAreaWidgetContents)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setMinimumSize(QSize(0, 50))
        self.passwd.setMaximumSize(QSize(16777215, 50))
        self.passwd__l = QHBoxLayout(self.passwd)
        self.passwd__l.setObjectName(u"passwd__l")

        self.verticalLayout_3.addWidget(self.passwd)

        self.age = QWidget(self.scrollAreaWidgetContents)
        self.age.setObjectName(u"age")
        self.age.setMinimumSize(QSize(0, 50))
        self.age.setMaximumSize(QSize(16777215, 50))
        self.age__l = QHBoxLayout(self.age)
        self.age__l.setObjectName(u"age__l")

        self.verticalLayout_3.addWidget(self.age)

        self.address = QWidget(self.scrollAreaWidgetContents)
        self.address.setObjectName(u"address")
        self.address.setMinimumSize(QSize(0, 50))
        self.address.setMaximumSize(QSize(16777215, 50))
        self.address__l = QHBoxLayout(self.address)
        self.address__l.setObjectName(u"address__l")

        self.verticalLayout_3.addWidget(self.address)

        self.telephone = QWidget(self.scrollAreaWidgetContents)
        self.telephone.setObjectName(u"telephone")
        self.telephone.setMinimumSize(QSize(0, 50))
        self.telephone.setMaximumSize(QSize(16777215, 50))
        self.telephone__l = QHBoxLayout(self.telephone)
        self.telephone__l.setObjectName(u"telephone__l")

        self.verticalLayout_3.addWidget(self.telephone)

        self.responsible = QWidget(self.scrollAreaWidgetContents)
        self.responsible.setObjectName(u"responsible")
        self.responsible.setMinimumSize(QSize(0, 50))
        self.responsible.setMaximumSize(QSize(16777215, 50))
        self.responsible__l = QHBoxLayout(self.responsible)
        self.responsible__l.setObjectName(u"responsible__l")

        self.verticalLayout_3.addWidget(self.responsible)

        self.photo_pix = QLabel(self.scrollAreaWidgetContents)
        self.photo_pix.setObjectName(u"photo_pix")
        self.photo_pix.setMinimumSize(QSize(0, 150))
        self.photo_pix.setMaximumSize(QSize(16777215, 150))
        self.photo_pix.setFont(font)
        self.photo_pix.setStyleSheet(u"font-size: 16pt")
        self.photo_pix.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.photo_pix)

        self.div = QLabel(self.scrollAreaWidgetContents)
        self.div.setObjectName(u"div")
        self.div.setMaximumSize(QSize(16777215, 167777))
        self.div.setFont(font)
        self.div.setStyleSheet(u"font-size: 16pt")
        self.div.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.div)

        self.photo_b = QWidget(self.scrollAreaWidgetContents)
        self.photo_b.setObjectName(u"photo_b")
        self.photo_b.setMinimumSize(QSize(0, 50))
        self.photo_b.setMaximumSize(QSize(16777215, 50))
        self.photo_b__l = QHBoxLayout(self.photo_b)
        self.photo_b__l.setObjectName(u"photo_b__l")

        self.verticalLayout_3.addWidget(self.photo_b)

        self.save_b = QWidget(self.scrollAreaWidgetContents)
        self.save_b.setObjectName(u"save_b")
        self.save_b.setMinimumSize(QSize(0, 50))
        self.save_b.setMaximumSize(QSize(16777215, 50))
        self.save_b__l = QHBoxLayout(self.save_b)
        self.save_b__l.setObjectName(u"save_b__l")

        self.verticalLayout_3.addWidget(self.save_b)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

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
        self.name_2.setText(QCoreApplication.translate("RightColumn", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.photo_pix.setText("")
        self.div.setText("")
        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Menu 2 - Right Menu", None))
    # retranslateUi

