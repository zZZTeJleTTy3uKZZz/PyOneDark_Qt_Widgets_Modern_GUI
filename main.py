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
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os


from gui.uis.windows.main_window.db_func import *
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    

    # ////////////////////////////////////////////////////////////////
    #                              Команда
    # ////////////////////////////////////////////////////////////////

    
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)
        
        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active
        # top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        # top_settings.set_active(False)

        

        # Левое меню
        # ///////////////////////////////////////////////////////////////

        # Домой
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.p_hub)
            SetupMainWindow.adaptive(self)
            if MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)
                self.ui.edit_btn.set_active(False)
                self.ui.add_btn.set_active(False)
            # print(MainFunctions.get_page(self))


        # Команда
        if btn.objectName() == "btn_team":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.p_team)
            SetupMainWindow.adaptive(self)
            if MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)
                self.ui.edit_btn.set_active(False)
                self.ui.add_btn.set_active(False)
            # print(MainFunctions.get_page(self))

        # Команда
        if btn.objectName() == "btn_storonnik":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.p_storonnik)
            SetupMainWindow.adaptive(self)
            if MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)
                self.ui.edit_btn.set_active(False)
                self.ui.add_btn.set_active(False)
            # print(MainFunctions.get_page(self))

        # Команда
        if btn.objectName() == "btn_event":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.p_event)
            SetupMainWindow.adaptive(self)
            if MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)
                self.ui.edit_btn.set_active(False)
                self.ui.add_btn.set_active(False)
            # print(MainFunctions.get_page(self))

        # Команда
        if btn.objectName() == "btn_kpi":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.p_kpi)
            SetupMainWindow.adaptive(self)
            if MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)
                self.ui.edit_btn.set_active(False)
                self.ui.add_btn.set_active(False)
            # print(MainFunctions.get_page(self))

        # Команда
        if btn.objectName() == "btn_quote":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.p_quote)
            SetupMainWindow.adaptive(self)
            if MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)
                self.ui.edit_btn.set_active(False)
                self.ui.add_btn.set_active(False)
            # print(MainFunctions.get_page(self))






        # BOTTOM INFORMATION
        if btn.objectName() == "btn_profile":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_leave" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            self.ui.left_menu.show()
            left_menu_margin = self.settings["left_menu_content_margins"]
            left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
            self.ui.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)
            
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            top_settings = MainFunctions.get_left_menu_btn(
                self, "btn_settings")
            top_settings.set_active_tab(False)

        if btn.objectName() == "btn_search":
            btn.hide()
            # Скрытие и раскрытие левого меню
            # profile = MainFunctions.get_title_bar_btn(self, "btn_profile")
            # profile.hide()
            # if self.ui.left_menu.isVisible():
            #     self.ui.left_menu_frame.setMinimumSize(0,0)
            #     self.ui.left_menu.hide()
            # else:
            #     left_menu_margin = self.settings["left_menu_content_margins"]
            #     left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
            #     self.ui.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)
            #     self.ui.left_menu.show()
            pass
        # DEBUG

        if btn.objectName() == "btn_top_add":
            self.ui.left_menu.show()
            left_menu_margin = self.settings["left_menu_content_margins"]
            left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
            self.ui.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)
            
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            top_settings = MainFunctions.get_left_menu_btn(
                self, "btn_top_add")
            top_settings.set_active_tab(False)


        if btn.objectName() == "btn_top_edit":
            self.ui.left_menu.show()
            left_menu_margin = self.settings["left_menu_content_margins"]
            left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
            self.ui.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)
            
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            top_settings = MainFunctions.get_left_menu_btn(
                self, "btn_top_edit")
            top_settings.set_active_tab(False)


        # print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        # print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())
