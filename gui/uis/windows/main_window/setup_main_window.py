# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////

from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from .functions_main_window import *
from gui.uis.windows.main_window.db_func import *
import sys
import os


# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from .ui_main import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *

from gui.core import *


ch = 0
select_item = ""
id_sel = -1


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Перейти на главную",
            "btn_tooltip": "Главная страница",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "_icon_team.svg",
            "btn_id": "btn_team",
            "btn_text": "Перейти к команде",
            "btn_tooltip": "Команда",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "_icon_storonniks.svg",
            "btn_id": "btn_storonnik",
            "btn_text": "Перейти к Сторонникам",
            "btn_tooltip": "Сторонники",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "_icon_event.svg",
            "btn_id": "btn_event",
            "btn_text": "Перейти к меропритиям",
            "btn_tooltip": "Мероприятия",
            "show_top": True,
            "is_active": False
        },
        # {
        #     "btn_icon": "_icon_task.svg",
        #     "btn_id": "btn_kpi",
        #     "btn_text": "Перейти к KPI",
        #     "btn_tooltip": "KPI",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "_icon_quote.svg",
        #     "btn_id": "btn_quote",
        #     "btn_text": "Добавить цитату",
        #     "btn_tooltip": "Цитаты",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "_icon_profile.svg",
        #     "btn_id": "btn_profile",
        #     "btn_text": "Открыть профиль",
        #     "btn_tooltip": "Профиль",
        #     "show_top": False,
        #     "is_active": False
        # },
        {
            "btn_icon": "_icon_leave.svg",
            "btn_id": "btn_leave",
            "btn_text": "Выйти из учётной записи",
            "btn_tooltip": "Выход",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    # add_title_bar_menus = [
    #     {
    #         "btn_icon" : "icon_search.svg",
    #         "btn_id" : "btn_search",
    #         "btn_tooltip" : "Search",
    #         "is_active" : False
    #     },
    #     {
    #         "btn_icon" : "icon_settings.svg",
    #         "btn_id" : "btn_top_settings",
    #         "btn_tooltip" : "Top settings",
    #         "is_active" : True
    #     }
    # ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////

    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(
                self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(
                self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        # self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Люди важнее!")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.p_hub)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(
            self, self.ui.right_column.users_menu)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ////////////////////////////////////////////////////////////////
        #                 Общее построение страницы с БД
        # ////////////////////////////////////////////////////////////////

        self.ui.add_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("_icon_add.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Создать запись",
            width=36,
            height=36,
            radius=12,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )

        self.ui.edit_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("_icon_edit.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Редактировать запись",
            width=36,
            height=36,
            radius=12,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["yellow"]
        )

        self.ui.delete_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("_icon_delete.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Удалить запись",
            width=36,
            height=36,
            radius=12,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )

        self.ui.export_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("_icon_export.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Экспорт в таблицу",
            width=36,
            height=36,
            radius=12,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )

        self.ui.search_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_search.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Поиск",
            width=36,
            height=36,
            radius=12,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )

        self.ui.action_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("_icon_action.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Добавить активность",
            width=36,
            height=36,
            radius=12,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )

        # Добавление таблицы

        self.ui.table = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["dark_three"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )

        # Поиск

        self.ui.find_l = PyLineEdit(
            text="",
            place_holder_text="Поиск",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
            is_active=False,
        )
        self.ui.find_l.setMinimumHeight(40)

        # Добавление объектов на главный пэйдж

        # ////////////////////////////////////////////////////////////////
        #                              Авторизация
        # ////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////
        #                              Главная
        # ////////////////////////////////////////////////////////////////

        # Добавление лого
        self.logo_svg = QSvgWidget(Functions.set_svg_image("stav.svg"))
        self.logo_svg.setFixedSize(350, 340)
        self.ui.load_pages.row_1_layout_7.addWidget(
            self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        self.ui.l_login_auth = PyLineEdit(
            text="",
            place_holder_text="Логин",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Логин",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_login_auth.setMinimumHeight(40)

        self.ui.l_passwd_auth = PyLineEdit(
            text="",
            place_holder_text="Пароль",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Пароль",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_passwd_auth.setMinimumHeight(40)
        self.ui.l_passwd_auth.setEchoMode(QLineEdit.Password)

        self.ui.b_auth = PyPushButton(
            text="Войти",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.b_auth.setMaximumHeight(40)
        self.ui.b_auth.setMinimumHeight(40)

        self.ui.b_spros = PyPushButton(
            text="Помощь",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.b_spros.setMaximumHeight(40)
        self.ui.b_spros.setMinimumHeight(40)

        self.ui.debug = QLabel()
        self.ui.debug.setText("Неправильный логин или пароль")
        self.ui.debug.setStyleSheet(u"font-size: 16pt")
        self.ui.debug.setAlignment(Qt.AlignCenter)

        self.ui.load_pages.row_2_layout_7.addWidget(self.ui.l_login_auth)
        self.ui.load_pages.row_3_layout_7.addWidget(self.ui.l_passwd_auth)
        self.ui.load_pages.row_4_layout_7.addWidget(self.ui.debug)
        self.ui.load_pages.row_5_layout_7.addWidget(self.ui.b_auth)
        self.ui.load_pages.row_5_layout_7.addWidget(self.ui.b_spros)

        # ////////////////////////////////////////////////////////////////
        #                              Команда
        # ////////////////////////////////////////////////////////////////

        # ------------------------------------------
        #               Правое меню
        # ------------------------------------------

        # ////////////////////////////////////////////////////////////////
        #                              Команда
        # ////////////////////////////////////////////////////////////////

        # Создание инпутов
        self.ui.l_l_name = PyLineEdit(
            text="",
            place_holder_text="Фамилия",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Фамилия",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_l_name.setMinimumHeight(40)

        self.ui.l_name = PyLineEdit(
            text="",
            place_holder_text="Имя",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Имя",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_name.setMinimumHeight(40)

        self.ui.c_table_role = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Роль",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        value = Role.select()
        dict_role = {}

        for val in value:
            dict_role.update({val.name: val.id})
        for ro in dict_role.keys():
            self.ui.c_table_role.addItem(ro)

        self.ui.l_login = PyLineEdit(
            text="",
            place_holder_text="Логин",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Логин",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_login.setMinimumHeight(40)

        self.ui.l_passwd = PyLineEdit(
            text="",
            place_holder_text="Пароль",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Пароль",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_passwd.setMinimumHeight(40)

        self.ui.l_age = PyLineEdit(
            text="",
            place_holder_text="Возраст",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Возраст",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_age.setMinimumHeight(40)

        self.ui.l_address = PyLineEdit(
            text="",
            place_holder_text="Адрес",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Адрес",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_address.setMinimumHeight(40)

        self.ui.l_telephone = PyLineEdit(
            text="",
            place_holder_text="Телефон",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Телефон",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_telephone.setMinimumHeight(40)

        self.ui.c_responsible = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Ответственный",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        users = User.select()
        dict_user = {}
        for us in users:
            user = f"{us.l_name} {us.name}"
            dict_user.update({user: us.id})
        for us in dict_user.keys():
            self.ui.c_responsible.addItem(us)

        self.ui.b_photo = PyPushButton(
            text="  Загрузить фото",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_file.svg"))
        self.ui.b_photo.setIcon(self.icon)
        self.ui.b_photo.setMaximumHeight(40)

        #  Добавление элементов на правое меню
        self.ui.right_column.l_name__l.addWidget(self.ui.l_l_name)
        self.ui.right_column.name__l.addWidget(self.ui.l_name)
        self.ui.right_column.table_role__l.addWidget(self.ui.c_table_role)
        self.ui.right_column.login__l.addWidget(self.ui.l_login)
        self.ui.right_column.passwd__l.addWidget(self.ui.l_passwd)
        self.ui.right_column.age__l.addWidget(self.ui.l_age)
        self.ui.right_column.address__l.addWidget(self.ui.l_address)
        self.ui.right_column.telephone__l.addWidget(self.ui.l_telephone)
        self.ui.right_column.responsible__l.addWidget(self.ui.c_responsible)
        self.ui.right_column.photo_b__l.addWidget(self.ui.b_photo)

        # ////////////////////////////////////////////////////////////////
        #                              Сторонники
        # ////////////////////////////////////////////////////////////////

        self.ui.l_l_name_2 = PyLineEdit(
            text="",
            place_holder_text="Фамилия",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Фамилия",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_l_name_2.setMinimumHeight(40)

        self.ui.l_name_2 = PyLineEdit(
            text="",
            place_holder_text="Имя",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Имя",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_name_2.setMinimumHeight(40)

        self.ui.l_age_2 = PyLineEdit(
            text="",
            place_holder_text="Возраст",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Возраст",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_age_2.setMinimumHeight(40)

        self.ui.l_address_2 = PyLineEdit(
            text="",
            place_holder_text="Адрес",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Адрес",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_address_2.setMinimumHeight(40)

        self.ui.l_telephone_2 = PyLineEdit(
            text="",
            place_holder_text="Телефон",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Телефон",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_telephone_2.setMinimumHeight(40)

        self.ui.l_social_2 = PyLineEdit(
            text="",
            place_holder_text="Социальные сети",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Социальные сети",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_social_2.setMinimumHeight(40)

        self.ui.c_responsible_2 = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Ответственный",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        users = User.select()
        dict_user = {}
        for us in users:
            user = f"{us.l_name} {us.name}"
            dict_user.update({user: us.id})
        for us in dict_user.keys():
            self.ui.c_responsible_2.addItem(us)

        self.ui.c_loyality_2 = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Лояльность",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        loyality = Loyality.select()
        dict_loyality = {}
        for lo in loyality:
            dict_loyality.update({lo.name: lo.id})
        for lo in dict_loyality.keys():
            self.ui.c_loyality_2.addItem(lo)

        self.ui.l_desc_2 = PyLineEdit(
            text="",
            place_holder_text="Описание",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Описание",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_desc_2.setMinimumHeight(40)

        self.ui.right_column.l_name__l_2.addWidget(self.ui.l_l_name_2)
        self.ui.right_column.name__l_2.addWidget(self.ui.l_name_2)
        self.ui.right_column.age__l_2.addWidget(self.ui.l_age_2)
        self.ui.right_column.address__l_2.addWidget(self.ui.l_address_2)
        self.ui.right_column.telephone__l_2.addWidget(self.ui.l_telephone_2)
        self.ui.right_column.social__l_2.addWidget(self.ui.l_social_2)
        self.ui.right_column.responsible__l_2.addWidget(
            self.ui.c_responsible_2)
        self.ui.right_column.loyality__l_2.addWidget(self.ui.c_loyality_2)
        self.ui.right_column.desc__l_2.addWidget(self.ui.l_desc_2)

        # ////////////////////////////////////////////////////////////////
        #                              Мероприятия
        # ////////////////////////////////////////////////////////////////
        self.ui.l_l_name_2.setMinimumHeight(40)

        self.ui.l_name_3 = PyLineEdit(
            text="",
            place_holder_text="Название",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Название",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_name_3.setMinimumHeight(40)

        self.ui.l_budget_3 = PyLineEdit(
            text="",
            place_holder_text="Бюджет",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Бюджет",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_budget_3.setMinimumHeight(40)

        self.ui.c_responsible_3 = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Ответственный",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        users = User.select()
        dict_user = {}
        for us in users:
            user = f"{us.l_name} {us.name}"
            dict_user.update({user: us.id})
        for us in dict_user.keys():
            self.ui.c_responsible_3.addItem(us)

        self.ui.c_type_3 = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Тип мероприятия",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        e_types = E_type.select()
        dict_types = {}
        for e in e_types:
            dict_types.update({e.name: e.id})
        for e in dict_types.keys():
            self.ui.c_type_3.addItem(e)

        self.ui.l_desc_3 = PyLineEdit(
            text="",
            place_holder_text="Описание",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Описание",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_desc_3.setMinimumHeight(40)

        self.ui.right_column.type__l_3.addWidget(self.ui.c_type_3)
        self.ui.right_column.name__l_3.addWidget(self.ui.l_name_3)
        self.ui.right_column.budget__l_3.addWidget(self.ui.l_budget_3)
        self.ui.right_column.responsible__l_3.addWidget(
            self.ui.c_responsible_3)

        self.ui.right_column.desc__l_3.addWidget(self.ui.l_desc_3)

        # ////////////////////////////////////////////////////////////////
        #                              Активность
        # ////////////////////////////////////////////////////////////////
        
        
        self.ui.l_address_4 = PyLineEdit(
            text="",
            place_holder_text="Адрес",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Адрес",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_address_4.setMinimumHeight(40)
        
        self.ui.l_date_4 = PyLineEdit(
            text="",
            place_holder_text="Дата",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Дата",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_date_4.setMinimumHeight(40)

        self.ui.l_desc_4 = PyLineEdit(
            text="",
            place_holder_text="Описание",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            app_parent=self.ui.central_widget,
            tooltip_text="Описание",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        self.ui.l_desc_4.setMinimumHeight(40)

        self.ui.c_e_type_4 = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Мероприятие",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        events = Event.select()
        dict_event = {}
        for e in events:
            dict_event.update({e.name: e.id})
        for e in dict_event.keys():
            self.ui.c_e_type_4.addItem(e)

        self.ui.c_s_type_4 = PyComboBox(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            app_parent=self.ui.central_widget,
            tooltip_text="Мероприятие",
            dark_one=self.themes["app_color"]["dark_one"],
            parent=self,
        )
        events = Storonnik.select()
        dict_stor = {}
        for e in events:
            name = f"{e.l_name} {e.name}"
            dict_stor.update({name: e.id})
        for e in dict_stor.keys():
            self.ui.c_s_type_4.addItem(e)

        self.ui.right_column.e_type__l_4.addWidget(self.ui.c_e_type_4)
        self.ui.right_column.storonnik__l_4.addWidget(self.ui.c_s_type_4)
        self.ui.right_column.address__l_4.addWidget(self.ui.l_address_4)
        self.ui.right_column.date__l_4.addWidget(
            self.ui.l_date_4)

        self.ui.right_column.desc__l_4.addWidget(self.ui.l_desc_4)




        # ////////////////////////////////////////////////////////////////
        #                              Цитаты
        # ////////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////
        #                 Общее построение правого меню
        # ////////////////////////////////////////////////////////////////

        self.ui.b_save = PyPushButton(
            text="Сохранить",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.b_save.setMaximumHeight(40)

        self.ui.b_cancel = PyPushButton(
            text="Отмена",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.b_cancel.setMaximumHeight(40)

        # ///////////////////////////////////////////////////////////////
        #                           функции
        # ///////////////////////////////////////////////////////////////

        # Общие

        # Выход из правого меню

        def cancel():
            MainFunctions.toggle_right_column(self)

        # Экспорт в Excel

        def export():
            if MainFunctions.get_page(self) == 1:
                exportxl("Команда")
            if MainFunctions.get_page(self) == 2:
                exportxl("Сторонники")
            if MainFunctions.get_page(self) == 3:
                exportxl("Мероприятия")

        # Добавление записи
        def add():
            if not MainFunctions.right_column_is_visible(self):
                global id_sel
                id_sel = -1
                if MainFunctions.get_page(self) == 1:

                    self.ui.l_l_name.setText(None)
                    self.ui.l_name.setText(None)
                    self.ui.c_table_role.setCurrentIndex(-1)
                    self.ui.l_login.setText(None)
                    self.ui.l_passwd.setText(None)
                    self.ui.l_age.setText(None)
                    self.ui.l_address.setText(None)
                    self.ui.l_telephone.setText(None)
                    self.ui.c_responsible.setCurrentIndex(-1)
                    MainFunctions.toggle_right_column(self)

                if MainFunctions.get_page(self) == 2:

                    self.ui.l_l_name_2.setText(None)
                    self.ui.l_name_2.setText(None)
                    self.ui.c_loyality_2.setCurrentIndex(-1)
                    self.ui.l_age_2.setText(None)
                    self.ui.l_address_2.setText(None)
                    self.ui.l_telephone_2.setText(None)
                    self.ui.c_responsible_2.setCurrentIndex(-1)
                    self.ui.l_desc_2.setText(None)
                    MainFunctions.toggle_right_column(self)

                if MainFunctions.get_page(self) == 3:

                    self.ui.l_name_3.setText(None)
                    self.ui.c_type_3.setCurrentIndex(-1)
                    self.ui.l_budget_3.setText(None)
                    self.ui.c_responsible_3.setCurrentIndex(-1)
                    self.ui.l_desc_3.setText(None)
                    MainFunctions.toggle_right_column(self)

        # Редактирование записи

        def edit():

            try:
                global id_sel
                for i in self.ui.table.selectedItems():
                    if MainFunctions.get_page(self) == 1:
                        id_sel = self.ui.table.item(
                            i.row(), len(self.ui.users)-1).text()
                    if MainFunctions.get_page(self) == 2:
                        id_sel = self.ui.table.item(
                            i.row(), len(self.ui.storoniks)-1).text()
                    if MainFunctions.get_page(self) == 3:
                        id_sel = self.ui.table.item(
                            i.row(), len(self.ui.events)-1).text()
                    if not MainFunctions.right_column_is_visible(self):

                        if MainFunctions.get_page(self) == 1:
                            team = User.select().where(User.id == id_sel)
                            for t in team:
                                self.ui.l_l_name.setText(t.l_name)
                                self.ui.l_name.setText(t.name)
                                self.ui.c_table_role.setCurrentIndex(
                                    t.role_id-1)
                                self.ui.l_login.setText(t.login)
                                self.ui.l_passwd.setText(t.passwd)
                                self.ui.l_age.setText(str(t.age))
                                self.ui.l_address.setText(t.address)
                                self.ui.l_telephone.setText(t.telephone)
                                self.find = int(t.responsible_id)
                                try:
                                    self.ui.right_column.photo_pix.setPixmap(
                                        show_image(id_sel))
                                except:
                                    self.ui.right_column.photo_pix.setText(
                                        "Нет фото")
                                    pass
                                if self.find in dict_user.values():
                                    cur_index = list(
                                        dict_user.values()).index(self.find)
                                self.ui.c_responsible.setCurrentIndex(
                                    cur_index)
                            MainFunctions.toggle_right_column(self)

                        if MainFunctions.get_page(self) == 2:
                            team = Storonnik.select().where(Storonnik.id == id_sel)
                            for t in team:
                                self.ui.l_l_name_2.setText(t.l_name)
                                self.ui.l_name_2.setText(t.name)
                                self.ui.c_loyality_2.setCurrentIndex(
                                    t.loyality_id-1)
                                self.ui.l_age_2.setText(str(t.age))
                                self.ui.l_address_2.setText(t.address)
                                self.ui.l_telephone_2.setText(t.telephone)
                                self.find = int(t.responsible_id)
                                if self.find in dict_user.values():
                                    cur_index = list(
                                        dict_user.values()).index(self.find)
                                self.ui.c_responsible_2.setCurrentIndex(
                                    cur_index)
                                self.ui.l_social_2.setText(t.social_media)
                                self.ui.l_desc_2.setText(t.desc)
                            MainFunctions.toggle_right_column(self)

                        if MainFunctions.get_page(self) == 3:
                            team = Event.select().where(Event.id == id_sel)
                            for t in team:
                                self.ui.l_name_3.setText(t.name)
                                self.ui.c_type_3.setCurrentIndex(
                                    t.e_type_id-1)
                                self.ui.l_budget_3.setText(str(t.budget))

                                self.find = int(t.responsible_id)
                                if self.find in dict_user.values():
                                    cur_index = list(
                                        dict_user.values()).index(self.find)
                                self.ui.c_responsible_3.setCurrentIndex(
                                    cur_index)
                                self.ui.l_desc_3.setText(t.desc)
                            MainFunctions.toggle_right_column(self)

            except:
                errors_sel()

        # Сохранение правое меню

        def save():
            global id_sel
            MainFunctions.toggle_right_column(self)

            if MainFunctions.get_page(self) == 1:
                l_name = self.ui.l_l_name.text()
                name = self.ui.l_name.text()
                role = self.ui.c_table_role.currentText()
                id_role = dict_role[role]
                login = self.ui.l_login.text()
                passwd = self.ui.l_passwd.text()
                age = int(self.ui.l_age.text())
                address = self.ui.l_address.text()
                telephone = self.ui.l_telephone.text()
                responsible = self.ui.c_responsible.currentText()
                id_responsible = dict_user[responsible]
                photo = self.ui.photo
                photo_path = self.ui.ospath

                if id_sel == -1:

                    db_user = {"l_name": l_name, "name": name, "login": login, "passwd": passwd,
                               "age": age, "address": address, "telephone": telephone, "role_id": id_role,
                               "responsible_id": id_responsible, "photo": photo, "photo_path": photo_path}
                    User.insert(db_user).execute()
                else:
                    for us in User.select().where(User.id == id_sel):
                        us.l_name = l_name
                        us.name = name
                        us.role_id = id_role
                        us.login = login
                        us.passwd = passwd
                        us.age = age
                        us.address = address
                        us.telephone = telephone
                        us.responsible_id = id_responsible
                        us.photo = photo
                        us.photo_path = photo_path
                        us.save()

                load_rows(self.ui.table, User(), 'User')

            if MainFunctions.get_page(self) == 2:
                l_name = self.ui.l_l_name_2.text()
                name = self.ui.l_name_2.text()
                loyality = self.ui.c_loyality_2.currentText()
                id_loyality = dict_loyality[loyality]
                age = int(self.ui.l_age_2.text())
                address = self.ui.l_address_2.text()
                telephone = self.ui.l_telephone_2.text()
                desc = self.ui.l_desc_2.text()
                social = self.ui.l_social_2.text()
                responsible = self.ui.c_responsible_2.currentText()
                id_responsible = dict_user[responsible]

                if id_sel == -1:

                    db_storonnik = {"l_name": l_name, "name": name,
                                    "age": age, "address": address, "telephone": telephone, "social_media": social, "loyality_id": id_loyality,
                                    "responsible_id": id_responsible, "desc": desc}
                    Storonnik.insert(db_storonnik).execute()
                else:
                    for us in Storonnik.select().where(Storonnik.id == id_sel):
                        us.l_name = l_name
                        us.name = name
                        us.loyality_id = id_loyality
                        us.age = age
                        us.address = address
                        us.telephone = telephone
                        us.responsible_id = id_responsible
                        us.social_media = social
                        us.desc = desc
                        us.save()

                load_rows(self.ui.table, Storonnik(), 'Storonnik')

            if MainFunctions.get_page(self) == 3:
                name = self.ui.l_name_3.text()
                types = self.ui.c_type_3.currentText()
                id_types = dict_types[types]
                budget = int(self.ui.l_budget_3.text())
                desc = self.ui.l_desc_3.text()
                responsible = self.ui.c_responsible_3.currentText()
                id_responsible = dict_user[responsible]

                if id_sel == -1:

                    db_event = {"e_type_id": id_types, "name": name,
                                "budget": budget,
                                "responsible_id": id_responsible, "desc": desc}
                    Event.insert(db_event).execute()
                else:
                    for us in Event.select().where(Event.id == id_sel):
                        us.name = name
                        us.e_types_id = id_types
                        us.budget = budget
                        us.responsible_id = id_responsible
                        us.desc = desc
                        us.save()

                load_rows(self.ui.table, Event(), 'Event')

        # Удаение записи
        def delete():
            try:
                global id_sel
                for i in self.ui.table.selectedItems():
                    id_sel = self.ui.table.item(
                        i.row(), len(self.ui.data)-1).text()
                    if not MainFunctions.right_column_is_visible(self):

                        if MainFunctions.get_page(self) == 1:
                            team = User.get(User.id == id_sel)
                            team.delete_instance()
                            load_rows(self.ui.table, User(), 'User')

                        if MainFunctions.get_page(self) == 2:
                            storonnik = Storonnik.get(Storonnik.id == id_sel)
                            storonnik.delete_instance()
                            load_rows(self.ui.table, Storonnik(), 'Storonnik')

                        if MainFunctions.get_page(self) == 3:
                            event = Event.get(Event.id == id_sel)
                            event.delete_instance()
                            load_rows(self.ui.table, Event(), 'Event')

            except:
                errors_sel()

        def search():
            global ch
            global select_item

            if select_item == self.ui.find_l.text():
                ch += 1
            else:
                ch = 0
                select_item = self.ui.find_l.text()
            self.ui.table.setCurrentItem(None)
            if not select_item:
                return

            try:
                search_item = self.ui.table.findItems(
                    select_item, Qt.MatchContains)
                if search_item:
                    try:
                        item = search_item[ch]
                        self.ui.table.setCurrentItem(item)
                    except:
                        ch = -1

            except:
                errors_sel()

        def action():
            MainFunctions.set_right_column_menu(
            self, self.ui.right_column.action_page)
            self.ui.right_column.e_type__l_4.addWidget(self.ui.c_e_type_4)
            self.ui.right_column.storonnik__l_4.addWidget(self.ui.c_s_type_4)
            self.ui.right_column.address__l_4.addWidget(self.ui.l_address_4)
            self.ui.right_column.date__l_4.addWidget(
                self.ui.l_date_4)

            self.ui.right_column.desc__l_4.addWidget(self.ui.l_desc_4)
            if not MainFunctions.right_column_is_visible(self):
                global id_sel
                id_sel = -1
                if MainFunctions.get_page(self) == 2 or 3:

                    self.ui.c_e_type_4.setCurrentIndex(-1)
                    self.ui.c_s_type_4.setCurrentIndex(-1)
                    self.ui.l_address_4.setText(None)
                    self.ui.l_date_4.setText(None)
                    self.ui.l_desc_4.setText(None)
                    MainFunctions.toggle_right_column(self)
            pass

        def exportxl(name):
            columnheaders = []
            date = QDate.currentDate().toString('dd-MM-yyyy')
            for j in range(self.ui.table.model().columnCount()):
                columnheaders.append(
                    self.ui.table.horizontalHeaderItem(j).text())

            df = pd.DataFrame(columns=columnheaders)

            for row in range(self.ui.table.rowCount()):
                for col in range(self.ui.table.columnCount()):
                    if MainFunctions.get_page(self) == 1:
                        if col == 0:

                            pass
                        else:
                            df.at[row, columnheaders[col]] = self.ui.table.item(
                                row, col).text()
                    else:
                        df.at[row, columnheaders[col]] = self.ui.table.item(
                            row, col).text()

            df.to_excel(f'{date} отчёт {name}.xlsx', index=False)

        # Команда

        def show_image(id_user=None, width=9999):
            if id_user != None:
                ph = User.select().where(User.id == id_user)
                for p in ph:
                    img = p.photo
                    ext = p.photo_path[p.photo_path.rfind(
                        '.'):len(p.photo_path)]
            else:
                img = self.ui.photo
                ext = self.ui.ospath
            self.pixmap = QPixmap()

            self.pixmap.loadFromData(img, ext)
            self.pixmap_resize = self.pixmap.scaled(
                130, width, Qt.KeepAspectRatio)
            return self.pixmap_resize

        def get_photo():
            fname = QFileDialog.getOpenFileName(self,
                                                'Choose picture',
                                                './')

            self.ui.ospath = fname[0]
            with open(self.ui.ospath, 'rb') as ph:
                self.ui.photo = ph.read()
            self.ui.right_column.photo_pix.setPixmap(show_image())

        # ///////////////////////////////////////////////////////////////
        #                           Сигналы
        # ///////////////////////////////////////////////////////////////

        # ----------------------- Главная форма --------------------------

        # Общие
        self.ui.add_btn.clicked.connect(lambda: add())
        self.ui.edit_btn.clicked.connect(lambda: edit())
        self.ui.delete_btn.clicked.connect(lambda: delete())
        self.ui.export_btn.clicked.connect(lambda: export())
        self.ui.search_btn.clicked.connect(lambda: search())
        self.ui.action_btn.clicked.connect(lambda: action())

        # ------------------------- Правое меню ----------------------------

        # Общие
        self.ui.b_save.clicked.connect(lambda: save())
        self.ui.b_cancel.clicked.connect(lambda: cancel())

        # Команда
        self.ui.b_photo.clicked.connect(lambda: get_photo())

    def adaptive(self):
        if MainFunctions.get_page(self) == 1:
            self.ui.load_pages.row_1_layout.addWidget(self.ui.table)
            self.ui.load_pages.row_2_layout.addWidget(self.ui.add_btn)
            self.ui.load_pages.row_2_layout.addWidget(self.ui.edit_btn)
            self.ui.load_pages.row_2_layout.addWidget(self.ui.delete_btn)
            self.ui.load_pages.row_2_layout.addWidget(self.ui.export_btn)
            self.ui.load_pages.row_2_layout.addWidget(self.ui.find_l)
            self.ui.load_pages.row_2_layout.addWidget(self.ui.search_btn)
            self.ui.right_column.save_b__l.addWidget(self.ui.b_save)
            self.ui.right_column.save_b__l.addWidget(self.ui.b_cancel)
            MainFunctions.set_right_column_menu(
                self, self.ui.right_column.users_menu)

        # ////////////////////////////////////////////////////////////////
        #                              Сторонники
        # ////////////////////////////////////////////////////////////////
        if MainFunctions.get_page(self) == 2:
            self.ui.load_pages.row_1_layout_2.addWidget(self.ui.table)
            self.ui.load_pages.row_2_layout_2.addWidget(self.ui.add_btn)
            self.ui.load_pages.row_2_layout_2.addWidget(self.ui.edit_btn)
            self.ui.load_pages.row_2_layout_2.addWidget(self.ui.delete_btn)
            self.ui.load_pages.row_2_layout_2.addWidget(self.ui.action_btn)
            self.ui.load_pages.row_2_layout_2.addWidget(self.ui.export_btn)
            self.ui.load_pages.row_2_layout_2.addWidget(self.ui.find_l)
            self.ui.load_pages.row_2_layout_2.addWidget(self.ui.search_btn)
            self.ui.right_column.save_b__l_2.addWidget(self.ui.b_save)
            self.ui.right_column.save_b__l_2.addWidget(self.ui.b_cancel)
            MainFunctions.set_right_column_menu(
                self, self.ui.right_column.storonik_menu)

        # ////////////////////////////////////////////////////////////////
        #                              Мероприятия
        # ////////////////////////////////////////////////////////////////
        if MainFunctions.get_page(self) == 3:
            self.ui.load_pages.row_1_layout_3.addWidget(self.ui.table)
            self.ui.load_pages.row_2_layout_3.addWidget(self.ui.add_btn)
            self.ui.load_pages.row_2_layout_3.addWidget(self.ui.edit_btn)
            self.ui.load_pages.row_2_layout_3.addWidget(self.ui.delete_btn)
            self.ui.load_pages.row_2_layout_3.addWidget(self.ui.action_btn)
            self.ui.load_pages.row_2_layout_3.addWidget(self.ui.export_btn)
            self.ui.load_pages.row_2_layout_3.addWidget(self.ui.find_l)
            self.ui.load_pages.row_2_layout_3.addWidget(self.ui.search_btn)
            self.ui.right_column.save_b__l_3.addWidget(self.ui.b_save)
            self.ui.right_column.save_b__l_3.addWidget(self.ui.b_cancel)
            MainFunctions.set_right_column_menu(
                self, self.ui.right_column.event_menu)

        # ////////////////////////////////////////////////////////////////
        #                              KPI
        # ////////////////////////////////////////////////////////////////
        if MainFunctions.get_page(self) == 4:
            self.ui.load_pages.row_1_layout_4.addWidget(self.ui.table)
            self.ui.load_pages.row_2_layout_4.addWidget(self.ui.add_btn)
            self.ui.load_pages.row_2_layout_4.addWidget(self.ui.edit_btn)
            self.ui.load_pages.row_2_layout_4.addWidget(self.ui.delete_btn)
            self.ui.load_pages.row_2_layout_4.addWidget(self.ui.export_btn)
            self.ui.load_pages.row_2_layout_4.addWidget(self.ui.find_l)
            self.ui.load_pages.row_2_layout_4.addWidget(self.ui.search_btn)

        # ////////////////////////////////////////////////////////////////
        #                              Цитаты
        # ////////////////////////////////////////////////////////////////
        if MainFunctions.get_page(self) == 5:
            self.ui.load_pages.row_1_layout_5.addWidget(self.ui.table)
            self.ui.load_pages.row_2_layout_5.addWidget(self.ui.add_btn)
            self.ui.load_pages.row_2_layout_5.addWidget(self.ui.edit_btn)
            self.ui.load_pages.row_2_layout_5.addWidget(self.ui.delete_btn)
            self.ui.load_pages.row_2_layout_5.addWidget(self.ui.export_btn)
            self.ui.load_pages.row_2_layout_5.addWidget(self.ui.find_l)
            self.ui.load_pages.row_2_layout_5.addWidget(self.ui.search_btn)

        # ///////////////////////////////////////////////////////////////
        #                           Данные
        # ///////////////////////////////////////////////////////////////

        # Заполнение таблицы

        # Команда
        if MainFunctions.get_page(self) == 1:
            self.ui.users = ("Фото", "Фамилия", "Имя", "Роль", "Логин", "Пароль",
                             "Возраст", "Адрес", "Телефон", "Ответственный", "photo_path", "id_user")
            deltable(self.ui.table)
            colum_header(self.ui.table, self.ui.users)
            load_rows(self.ui.table, User(), 'User')
            self.ui.data = self.ui.users

        # Сторонники
        if MainFunctions.get_page(self) == 2:
            self.ui.storoniks = ("Фамилия", "Имя",
                                 "Возраст", "Адрес", "Телефон", "Социальные сети", "Ответственный", "Лояльность", "Кол-во мероприятий", "Описание" "id_storonik")
            deltable(self.ui.table)
            colum_header(self.ui.table, self.ui.storoniks)
            load_rows(self.ui.table, Storonnik(), 'Storonnik')
            self.ui.data = self.ui.storoniks

        # Мероприятия
        if MainFunctions.get_page(self) == 3:
            self.ui.events = ("Тип мероприятия", "Название", "Бюджет",
                              "Ответственный", "Участников", "Описание", "id_event")
            deltable(self.ui.table)
            colum_header(self.ui.table, self.ui.events)
            load_rows(self.ui.table, Event(), 'Event')
            self.ui.data = self.ui.events

        # KPI
        if MainFunctions.get_page(self) == 4:
            self.ui.kpis = ("Название", "Кол-во", "Дедлайн",
                            "Цель", "Описание", "id_kpi")
            deltable(self.ui.table)
            colum_header(self.ui.table, self.ui.kpis)
            load_rows(self.ui.table, Kpi(), 'Kpi')
            self.ui.data = self.ui.kpis

        # Цитаты
        if MainFunctions.get_page(self) == 5:
            self.ui.quotes = ("Текст", "id_quote")
            deltable(self.ui.table)
            colum_header(self.ui.table, self.ui.quotes)
            load_rows(self.ui.table, Quote(), 'Quote')
            self.ui.data = self.ui.quotes

        print(MainFunctions.get_page(self))
        pass

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(
                self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(
                5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(
                self.width() - 20, self.height() - 20, 15, 15)
