# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_column.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from gui.core.json_themes import Themes

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        themes = Themes()
        self.themes = themes.items
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(219, 627)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1, 182, 795))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.u_label = QLabel(self.scrollAreaWidgetContents)
        self.u_label.setObjectName(u"u_label")
        self.u_label.setMinimumSize(QSize(0, 30))
        self.u_label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(16)
        self.u_label.setFont(font)
        self.u_label.setStyleSheet(u"font-size: 16pt")
        self.u_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.u_label)

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
        self.event_menu = QWidget()
        self.event_menu.setObjectName(u"event_menu")
        self.verticalLayout_6 = QVBoxLayout(self.event_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_3 = PyScrollArea(self.users_menu,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        )
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 191, 725))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.e_label = QLabel(self.scrollAreaWidgetContents_3)
        self.e_label.setObjectName(u"e_label")
        self.e_label.setMinimumSize(QSize(0, 30))
        self.e_label.setMaximumSize(QSize(16777215, 30))
        self.e_label.setFont(font)
        self.e_label.setStyleSheet(u"font-size: 16pt")
        self.e_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.e_label)

        self.type_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.type_3.setObjectName(u"type_3")
        self.type_3.setMinimumSize(QSize(0, 50))
        self.type_3.setMaximumSize(QSize(16777215, 50))
        self.type__l_3 = QHBoxLayout(self.type_3)
        self.type__l_3.setObjectName(u"type__l_3")

        self.verticalLayout_5.addWidget(self.type_3)

        self.name_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.name_3.setObjectName(u"name_3")
        self.name_3.setMinimumSize(QSize(0, 50))
        self.name_3.setMaximumSize(QSize(16777215, 50))
        self.name__l_3 = QHBoxLayout(self.name_3)
        self.name__l_3.setObjectName(u"name__l_3")

        self.verticalLayout_5.addWidget(self.name_3)

        self.budget_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.budget_3.setObjectName(u"budget_3")
        self.budget_3.setMinimumSize(QSize(0, 50))
        self.budget_3.setMaximumSize(QSize(16777215, 50))
        self.budget__l_3 = QHBoxLayout(self.budget_3)
        self.budget__l_3.setObjectName(u"budget__l_3")

        self.verticalLayout_5.addWidget(self.budget_3)

        self.responsible_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.responsible_3.setObjectName(u"responsible_3")
        self.responsible_3.setMinimumSize(QSize(0, 50))
        self.responsible_3.setMaximumSize(QSize(16777215, 50))
        self.responsible__l_3 = QHBoxLayout(self.responsible_3)
        self.responsible__l_3.setObjectName(u"responsible__l_3")

        self.verticalLayout_5.addWidget(self.responsible_3)

        self.desc_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.desc_3.setObjectName(u"desc_3")
        self.desc_3.setMinimumSize(QSize(0, 50))
        self.desc_3.setMaximumSize(QSize(16777215, 50))
        self.desc__l_3 = QHBoxLayout(self.desc_3)
        self.desc__l_3.setObjectName(u"desc__l_3")

        self.verticalLayout_5.addWidget(self.desc_3)

        self.div_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.div_3.setObjectName(u"div_3")
        self.div_3.setMinimumSize(QSize(0, 20))
        self.div_3.setMaximumSize(QSize(16777215, 16777))
        self.div_3.setFont(font)
        self.div_3.setStyleSheet(u"font-size: 16pt")
        self.div_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.div_3)

        self.save_b_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.save_b_3.setObjectName(u"save_b_3")
        self.save_b_3.setMinimumSize(QSize(0, 50))
        self.save_b_3.setMaximumSize(QSize(16777215, 50))
        self.save_b__l_3 = QHBoxLayout(self.save_b_3)
        self.save_b__l_3.setObjectName(u"save_b__l_3")

        self.verticalLayout_5.addWidget(self.save_b_3)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea_3)

        self.menus.addWidget(self.event_menu)
        self.storonik_menu = QWidget()
        self.storonik_menu.setObjectName(u"storonik_menu")
        self.verticalLayout_2 = QVBoxLayout(self.storonik_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = PyScrollArea(self.users_menu,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        )
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 191, 725))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.s_label = QLabel(self.scrollAreaWidgetContents_2)
        self.s_label.setObjectName(u"s_label")
        self.s_label.setMinimumSize(QSize(0, 30))
        self.s_label.setMaximumSize(QSize(16777215, 30))
        self.s_label.setFont(font)
        self.s_label.setStyleSheet(u"font-size: 16pt")
        self.s_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.s_label)

        self.l_name_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.l_name_2.setObjectName(u"l_name_2")
        self.l_name_2.setMinimumSize(QSize(0, 50))
        self.l_name_2.setMaximumSize(QSize(16777215, 50))
        self.l_name__l_2 = QHBoxLayout(self.l_name_2)
        self.l_name__l_2.setObjectName(u"l_name__l_2")

        self.verticalLayout_4.addWidget(self.l_name_2)

        self.name_4 = QWidget(self.scrollAreaWidgetContents_2)
        self.name_4.setObjectName(u"name_4")
        self.name_4.setMinimumSize(QSize(0, 50))
        self.name_4.setMaximumSize(QSize(16777215, 50))
        self.name__l_2 = QHBoxLayout(self.name_4)
        self.name__l_2.setObjectName(u"name__l_2")

        self.verticalLayout_4.addWidget(self.name_4)

        self.age_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.age_2.setObjectName(u"age_2")
        self.age_2.setMinimumSize(QSize(0, 50))
        self.age_2.setMaximumSize(QSize(16777215, 50))
        self.age__l_2 = QHBoxLayout(self.age_2)
        self.age__l_2.setObjectName(u"age__l_2")

        self.verticalLayout_4.addWidget(self.age_2)

        self.address_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.address_2.setObjectName(u"address_2")
        self.address_2.setMinimumSize(QSize(0, 50))
        self.address_2.setMaximumSize(QSize(16777215, 50))
        self.address__l_2 = QHBoxLayout(self.address_2)
        self.address__l_2.setObjectName(u"address__l_2")

        self.verticalLayout_4.addWidget(self.address_2)

        self.telephone_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.telephone_2.setObjectName(u"telephone_2")
        self.telephone_2.setMinimumSize(QSize(0, 50))
        self.telephone_2.setMaximumSize(QSize(16777215, 50))
        self.telephone__l_2 = QHBoxLayout(self.telephone_2)
        self.telephone__l_2.setObjectName(u"telephone__l_2")

        self.verticalLayout_4.addWidget(self.telephone_2)

        self.social_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.social_2.setObjectName(u"social_2")
        self.social_2.setMinimumSize(QSize(0, 50))
        self.social_2.setMaximumSize(QSize(16777215, 50))
        self.social__l_2 = QHBoxLayout(self.social_2)
        self.social__l_2.setObjectName(u"social__l_2")

        self.verticalLayout_4.addWidget(self.social_2)

        self.responsible_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.responsible_2.setObjectName(u"responsible_2")
        self.responsible_2.setMinimumSize(QSize(0, 50))
        self.responsible_2.setMaximumSize(QSize(16777215, 50))
        self.responsible__l_2 = QHBoxLayout(self.responsible_2)
        self.responsible__l_2.setObjectName(u"responsible__l_2")

        self.verticalLayout_4.addWidget(self.responsible_2)

        self.loyality_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.loyality_2.setObjectName(u"loyality_2")
        self.loyality_2.setMinimumSize(QSize(0, 50))
        self.loyality_2.setMaximumSize(QSize(16777215, 50))
        self.loyality__l_2 = QHBoxLayout(self.loyality_2)
        self.loyality__l_2.setObjectName(u"loyality__l_2")

        self.verticalLayout_4.addWidget(self.loyality_2)

        self.desc_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.desc_2.setObjectName(u"desc_2")
        self.desc_2.setMinimumSize(QSize(0, 50))
        self.desc_2.setMaximumSize(QSize(16777215, 50))
        self.desc__l_2 = QHBoxLayout(self.desc_2)
        self.desc__l_2.setObjectName(u"desc__l_2")

        self.verticalLayout_4.addWidget(self.desc_2)

        self.div_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.div_2.setObjectName(u"div_2")
        self.div_2.setMinimumSize(QSize(0, 20))
        self.div_2.setMaximumSize(QSize(16777215, 16777))
        self.div_2.setFont(font)
        self.div_2.setStyleSheet(u"font-size: 16pt")
        self.div_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.div_2)

        self.save_b_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.save_b_2.setObjectName(u"save_b_2")
        self.save_b_2.setMinimumSize(QSize(0, 50))
        self.save_b_2.setMaximumSize(QSize(16777215, 50))
        self.save_b__l_2 = QHBoxLayout(self.save_b_2)
        self.save_b__l_2.setObjectName(u"save_b__l_2")

        self.verticalLayout_4.addWidget(self.save_b_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.menus.addWidget(self.storonik_menu)
        self.action_page = QWidget()
        self.action_page.setObjectName(u"action_page")
        self.verticalLayout_8 = QVBoxLayout(self.action_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_4 = PyScrollArea(self.users_menu,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        )
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QFrame.Plain)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 191, 599))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.a_label = QLabel(self.scrollAreaWidgetContents_4)
        self.a_label.setObjectName(u"a_label")
        self.a_label.setMinimumSize(QSize(0, 30))
        self.a_label.setMaximumSize(QSize(16777215, 30))
        self.a_label.setFont(font)
        self.a_label.setStyleSheet(u"font-size: 16pt")
        self.a_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.a_label)

        self.e_type_4 = QWidget(self.scrollAreaWidgetContents_4)
        self.e_type_4.setObjectName(u"e_type_4")
        self.e_type_4.setMinimumSize(QSize(0, 50))
        self.e_type_4.setMaximumSize(QSize(16777215, 50))
        self.e_type__l_4 = QHBoxLayout(self.e_type_4)
        self.e_type__l_4.setObjectName(u"e_type__l_4")

        self.verticalLayout_7.addWidget(self.e_type_4)

        self.storonnik_4 = QWidget(self.scrollAreaWidgetContents_4)
        self.storonnik_4.setObjectName(u"storonnik_4")
        self.storonnik_4.setMinimumSize(QSize(0, 50))
        self.storonnik_4.setMaximumSize(QSize(16777215, 50))
        self.storonnik__l_4 = QHBoxLayout(self.storonnik_4)
        self.storonnik__l_4.setObjectName(u"storonnik__l_4")

        self.verticalLayout_7.addWidget(self.storonnik_4)

        self.address_4 = QWidget(self.scrollAreaWidgetContents_4)
        self.address_4.setObjectName(u"address_4")
        self.address_4.setMinimumSize(QSize(0, 50))
        self.address_4.setMaximumSize(QSize(16777215, 50))
        self.address__l_4 = QHBoxLayout(self.address_4)
        self.address__l_4.setObjectName(u"address__l_4")

        self.verticalLayout_7.addWidget(self.address_4)

        self.date_4 = QWidget(self.scrollAreaWidgetContents_4)
        self.date_4.setObjectName(u"date_4")
        self.date_4.setMinimumSize(QSize(0, 170))
        self.date_4.setMaximumSize(QSize(16777215, 1666667))
        self.date__l_4 = QHBoxLayout(self.date_4)
        self.date__l_4.setObjectName(u"date__l_4")

        self.verticalLayout_7.addWidget(self.date_4)

        self.desc_4 = QWidget(self.scrollAreaWidgetContents_4)
        self.desc_4.setObjectName(u"desc_4")
        self.desc_4.setMinimumSize(QSize(0, 50))
        self.desc_4.setMaximumSize(QSize(16777215, 50))
        self.desc__l_4 = QHBoxLayout(self.desc_4)
        self.desc__l_4.setObjectName(u"desc__l_4")

        self.verticalLayout_7.addWidget(self.desc_4)

        self.div_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.div_4.setObjectName(u"div_4")
        self.div_4.setMinimumSize(QSize(0, 20))
        self.div_4.setMaximumSize(QSize(16777215, 16777))
        self.div_4.setFont(font)
        self.div_4.setStyleSheet(u"font-size: 16pt")
        self.div_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.div_4)

        self.save_b_4 = QWidget(self.scrollAreaWidgetContents_4)
        self.save_b_4.setObjectName(u"save_b_4")
        self.save_b_4.setMinimumSize(QSize(0, 50))
        self.save_b_4.setMaximumSize(QSize(16777215, 50))
        self.save_b__l_4 = QHBoxLayout(self.save_b_4)
        self.save_b__l_4.setObjectName(u"save_b__l_4")

        self.verticalLayout_7.addWidget(self.save_b_4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_8.addWidget(self.scrollArea_4)

        self.menus.addWidget(self.action_page)
        self.kpi_menu = QWidget()
        self.kpi_menu.setObjectName(u"kpi_menu")
        self.verticalLayout_10 = QVBoxLayout(self.kpi_menu)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_5 = PyScrollArea(self.users_menu,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        )
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setFrameShadow(QFrame.Plain)
        self.scrollArea_5.setLineWidth(0)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 191, 599))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.a_label_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.a_label_2.setObjectName(u"a_label_2")
        self.a_label_2.setMinimumSize(QSize(0, 30))
        self.a_label_2.setMaximumSize(QSize(16777215, 30))
        self.a_label_2.setFont(font)
        self.a_label_2.setStyleSheet(u"font-size: 16pt")
        self.a_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.a_label_2)

        self.name_5 = QWidget(self.scrollAreaWidgetContents_5)
        self.name_5.setObjectName(u"name_5")
        self.name_5.setMinimumSize(QSize(0, 50))
        self.name_5.setMaximumSize(QSize(16777215, 50))
        self.name__l_5 = QHBoxLayout(self.name_5)
        self.name__l_5.setObjectName(u"name__l_5")

        self.verticalLayout_9.addWidget(self.name_5)

        self.count_5 = QWidget(self.scrollAreaWidgetContents_5)
        self.count_5.setObjectName(u"count_5")
        self.count_5.setMinimumSize(QSize(0, 50))
        self.count_5.setMaximumSize(QSize(16777215, 50))
        self.count__l_5 = QHBoxLayout(self.count_5)
        self.count__l_5.setObjectName(u"count__l_5")

        self.verticalLayout_9.addWidget(self.count_5)

        self.object_5 = QWidget(self.scrollAreaWidgetContents_5)
        self.object_5.setObjectName(u"object_5")
        self.object_5.setMinimumSize(QSize(0, 50))
        self.object_5.setMaximumSize(QSize(16777215, 50))
        self.object__l_5 = QHBoxLayout(self.object_5)
        self.object__l_5.setObjectName(u"object__l_5")

        self.verticalLayout_9.addWidget(self.object_5)

        self.date_5 = QWidget(self.scrollAreaWidgetContents_5)
        self.date_5.setObjectName(u"date_5")
        self.date_5.setMinimumSize(QSize(0, 170))
        self.date_5.setMaximumSize(QSize(16777215, 1666667))
        self.date__l_5 = QHBoxLayout(self.date_5)
        self.date__l_5.setObjectName(u"date__l_5")

        self.verticalLayout_9.addWidget(self.date_5)

        self.desc_5 = QWidget(self.scrollAreaWidgetContents_5)
        self.desc_5.setObjectName(u"desc_5")
        self.desc_5.setMinimumSize(QSize(0, 50))
        self.desc_5.setMaximumSize(QSize(16777215, 50))
        self.desc__l_5 = QHBoxLayout(self.desc_5)
        self.desc__l_5.setObjectName(u"desc__l_5")

        self.verticalLayout_9.addWidget(self.desc_5)

        self.div_5 = QLabel(self.scrollAreaWidgetContents_5)
        self.div_5.setObjectName(u"div_5")
        self.div_5.setMinimumSize(QSize(0, 20))
        self.div_5.setMaximumSize(QSize(16777215, 16777))
        self.div_5.setFont(font)
        self.div_5.setStyleSheet(u"font-size: 16pt")
        self.div_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.div_5)

        self.save_b_5 = QWidget(self.scrollAreaWidgetContents_5)
        self.save_b_5.setObjectName(u"save_b_5")
        self.save_b_5.setMinimumSize(QSize(0, 50))
        self.save_b_5.setMaximumSize(QSize(16777215, 50))
        self.save_b__l_5 = QHBoxLayout(self.save_b_5)
        self.save_b__l_5.setObjectName(u"save_b__l_5")

        self.verticalLayout_9.addWidget(self.save_b_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_10.addWidget(self.scrollArea_5)

        self.menus.addWidget(self.kpi_menu)
        self.quote_menu = QWidget()
        self.quote_menu.setObjectName(u"quote_menu")
        self.verticalLayout_12 = QVBoxLayout(self.quote_menu)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_6 = PyScrollArea(self.users_menu,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
        )
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setFrameShape(QFrame.NoFrame)
        self.scrollArea_6.setFrameShadow(QFrame.Plain)
        self.scrollArea_6.setLineWidth(0)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 191, 599))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.a_label_3 = QLabel(self.scrollAreaWidgetContents_6)
        self.a_label_3.setObjectName(u"a_label_3")
        self.a_label_3.setMinimumSize(QSize(0, 30))
        self.a_label_3.setMaximumSize(QSize(16777215, 30))
        self.a_label_3.setFont(font)
        self.a_label_3.setStyleSheet(u"font-size: 16pt")
        self.a_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.a_label_3)

        self.text_6 = QWidget(self.scrollAreaWidgetContents_6)
        self.text_6.setObjectName(u"text_6")
        self.text_6.setMinimumSize(QSize(0, 50))
        self.text_6.setMaximumSize(QSize(16777215, 50))
        self.text__l_6 = QHBoxLayout(self.text_6)
        self.text__l_6.setObjectName(u"text__l_6")

        self.verticalLayout_11.addWidget(self.text_6)

        self.div_6 = QLabel(self.scrollAreaWidgetContents_6)
        self.div_6.setObjectName(u"div_6")
        self.div_6.setMinimumSize(QSize(0, 20))
        self.div_6.setMaximumSize(QSize(16777215, 16777))
        self.div_6.setFont(font)
        self.div_6.setStyleSheet(u"font-size: 16pt")
        self.div_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.div_6)

        self.save_b_6 = QWidget(self.scrollAreaWidgetContents_6)
        self.save_b_6.setObjectName(u"save_b_6")
        self.save_b_6.setMinimumSize(QSize(0, 50))
        self.save_b_6.setMaximumSize(QSize(16777215, 50))
        self.save_b__l_6 = QHBoxLayout(self.save_b_6)
        self.save_b__l_6.setObjectName(u"save_b__l_6")

        self.verticalLayout_11.addWidget(self.save_b_6)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_12.addWidget(self.scrollArea_6)

        self.menus.addWidget(self.quote_menu)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.u_label.setText(QCoreApplication.translate("RightColumn", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.photo_pix.setText("")
        self.div.setText("")
        self.e_label.setText(QCoreApplication.translate("RightColumn", u"\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435", None))
        self.div_3.setText("")
        self.s_label.setText(QCoreApplication.translate("RightColumn", u"\u0421\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u043a", None))
        self.div_2.setText("")
        self.a_label.setText(QCoreApplication.translate("RightColumn", u"\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.div_4.setText("")
        self.a_label_2.setText(QCoreApplication.translate("RightColumn", u"KPI", None))
        self.div_5.setText("")
        self.a_label_3.setText(QCoreApplication.translate("RightColumn", u"\u0426\u0438\u0442\u0430\u0442\u0430", None))
        self.div_6.setText("")
    # retranslateUi

