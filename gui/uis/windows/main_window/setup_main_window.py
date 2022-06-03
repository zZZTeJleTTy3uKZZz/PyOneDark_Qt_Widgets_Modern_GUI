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
from .db_func import *
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
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "только не на лицо",
            "btn_tooltip" : "Главная страница",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "_icon_team.svg",
            "btn_id" : "btn_team",
            "btn_text" : "Перейти к команде",
            "btn_tooltip" : "Команда",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "_icon_profile.svg",
            "btn_id" : "btn_profile",
            "btn_text" : "Открыть профиль",
            "btn_tooltip" : "Профиль",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "_icon_leave.svg",
            "btn_id" : "btn_leave",
            "btn_text" : "Выйти из очка",
            "btn_tooltip" : "Очко",
            "show_top" : False,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : True
        }
    ]

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
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

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
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

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
        MainFunctions.set_page(self, self.ui.load_pages.p_team)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.users_menu)

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
        #                              Авторизация
        # ////////////////////////////////////////////////////////////////
       
       
       
       
        # ////////////////////////////////////////////////////////////////
        #                              Главная
        # ////////////////////////////////////////////////////////////////

        
        # Добавление лого
        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        self.bt = QPushButton("Нажми на меня")
        def pr():
            print(self.ui.credits.copyright_label.text())

        self.bt.clicked.connect(lambda: pr())

        self.ui.load_pages.logo_layout.addWidget(self.bt)

        # ////////////////////////////////////////////////////////////////
        #                              Команда
        # ////////////////////////////////////////////////////////////////

        # Добавление кнопок
        """
        Хорошая попытка, но не сегодня(

        add_btn_user = [
        {
            "btn_icon" : "_icon_add.svg",
            "btn_id" : "btn_add_user",
            "btn_tooltip" : "Создать запись",
        },
        {
            "btn_icon" : "_icon_edit.svg",
            "btn_id" : "btn_edit_user",
            "btn_tooltip" : "Редактировать запись",
        },
        {
            "btn_icon" : "_icon_delete.svg",
            "btn_id" : "btn_del_user",
            "btn_tooltip" : "Удалить запись",
        },
        {
            "btn_icon" : "_icon_export.svg",
            "btn_id" : "btn_export_user",
            "btn_tooltip" : "Экспорт в таблицу",
        }
        ]

        self.ui.set_btn(add_btn_user)
        """

        
        self.add_btn = PyIconButton(
            icon_path = Functions.set_svg_icon("_icon_add.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Создать запись",
            width = 36,
            height = 36,
            radius = 12,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )

        self.edit_btn = PyIconButton(
            icon_path = Functions.set_svg_icon("_icon_edit.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Редактировать запись",
            width = 36,
            height = 36,
            radius = 12,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["yellow"]
        )

        self.delete_btn = PyIconButton(
            icon_path = Functions.set_svg_icon("_icon_delete.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Удалить запись",
            width = 36,
            height = 36,
            radius = 12,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )
        
        self.export_btn = PyIconButton(
            icon_path = Functions.set_svg_icon("_icon_export.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Экспорт в таблицу",
            width = 36,
            height = 36,
            radius = 12,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )


        # Добавление таблицы

        self.table_user = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        

        # Заполнение таблицы
        self.users = ("Фото", "Фамилия", "име", "Роль", "Логин", "Пароль", "Возраст", "Адрес", "Телефон", "Ответственный", "photo_path", "id_user")
        colum_header(self.table_user, self.users)  
        load_rows(self.table_user, User(), 'User')


        # Поиск

        self.find_l = PyLineEdit(
            text = "",
            place_holder_text = "Поиск",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.find_l.setMinimumHeight(40)

        # Добавление объектов на главный пэйдж
        self.ui.load_pages.row_1_layout.addWidget(self.table_user)
        self.ui.load_pages.row_2_layout.addWidget(self.add_btn)
        self.ui.load_pages.row_2_layout.addWidget(self.edit_btn)
        self.ui.load_pages.row_2_layout.addWidget(self.delete_btn)
        self.ui.load_pages.row_2_layout.addWidget(self.export_btn)
        self.ui.load_pages.row_2_layout.addWidget(self.find_l)


        # Функции

        def open_team_p():

            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        self.add_btn.clicked.connect(lambda: open_team_p())



        # ------------------------------------------
        #               Правое меню
        # ------------------------------------------

        # Создание инпутов
        self.l_l_name = PyLineEdit(
            text = "",
            place_holder_text = "Фамилия",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.l_l_name.setMinimumHeight(40)

        self.l_name = PyLineEdit(
            text = "",
            place_holder_text = "Имя",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.l_name.setMinimumHeight(40)

        self.l_login = PyLineEdit(
            text = "",
            place_holder_text = "Логин",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.l_login.setMinimumHeight(40)


        #  Добавление элементов на правое меню
        self.ui.right_column.l_name__l.addWidget(self.l_l_name)
        self.ui.right_column.name__l.addWidget(self.l_name)
        self.ui.right_column.login__l.addWidget(self.l_login)


        



        # ////////////////////////////////////////////////////////////////
        #                              Сторонники
        # ////////////////////////////////////////////////////////////////


        # ////////////////////////////////////////////////////////////////
        #                              Мероприятия
        # ////////////////////////////////////////////////////////////////


        # ////////////////////////////////////////////////////////////////
        #                              KPI
        # ////////////////////////////////////////////////////////////////


        # ////////////////////////////////////////////////////////////////
        #                              Цитаты
        # ////////////////////////////////////////////////////////////////


        


        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

