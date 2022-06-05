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

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QComboBox {{
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
	min-height: 38px;
	font-size: 12px;
	padding-left: 15 px;
}}


QComboBox::drop-down {{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 25px;

     border-left-width: 2px;
     border-left-color: {_context_color};
     border-left-style: solid; 
     border-top-right-radius: {_radius}px; 
     border-bottom-right-radius: {_radius}px;
 }}

QComboBox::down-arrow {{
     image: url(/down.png);
}}

QComboBox:hover {{
	background-color: {_bg_color_hover};
    
}}
QComboBox:pressed {{
	background-color: {_bg_color_pressed};
    
}}


 QComboBox QAbstractItemView {{
    selection-background-color: {_bg_color_pressed};
    color: {_color};
	background-color: {_bg_color};
	padding-left: 10 px;
	
	border-radius: {_radius}px;
 }}


QScrollBar:horizontal {{
    border: none;
    background: {_scroll_bar_bg_color};
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {_context_color};
    min-width: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: {_scroll_bar_btn_color};
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background: {_scroll_bar_btn_color};
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     background: none;
}}
QScrollBar:vertical {{
	border: none;
    background: {_scroll_bar_bg_color};
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{	
	background: {_context_color};
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     border: none;
    background: {_scroll_bar_btn_color};
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	border: none;
    background: {_scroll_bar_btn_color};
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
}} 
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyComboBox(QComboBox):
    def __init__(
        self, 
        radius,
        border_size,
        color,
        bg_color,
        bg_color_hover,
        bg_color_pressed,
        context_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        dark_one="#1b1e23",
        text_foreground="#8a95aa",
        app_parent=None,
        parent=None,
        top_margin=20,
        tooltip_text="",
    ):
        super().__init__()

        self._bg_color = bg_color
        self._bg_color_active = bg_color_hover
        self._parent = parent
        self._app_parent = app_parent
        self._top_margin = top_margin

        # TOOLTIP
        self._tooltip_text = tooltip_text
        self._tooltip = _ToolTip(
            app_parent,
            tooltip_text,
            dark_one,
            text_foreground
        )
        self._tooltip.hide()


        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
            _radius = radius,
            _border_size = border_size,
            _bg_color = bg_color,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed,
            _context_color = context_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
        )
        self.setStyleSheet(custom_style)

    
    def change_style(self, event):
        if event == QEvent.Enter:
            self._set_bg_color = self._bg_color_active
            self.repaint()
        elif event == QEvent.Leave:
            self._set_bg_color = self._bg_color
            self.repaint()


    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        self.move_tooltip()
        self._tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        self.move_tooltip()
        self._tooltip.hide()

    
    def move_tooltip(self):
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        # pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2)
        # pos_y = pos.y() - self._top_margin

        pos_x = pos.x() - (self._tooltip.width() + self._top_margin)
       
        pos_y =  (pos.y() - (self._tooltip.height() // 2)) + (self.height() // 2)

        # SET POSITION TO WIDGET
        # Move tooltip position
        self._tooltip.move(pos_x, pos_y)

# TOOLTIP
# ///////////////////////////////////////////////////////////////


class _ToolTip(QLabel):
    # TOOLTIP / LABEL StyleSheet
    style_tooltip = """ 
    QLabel {{		
        background-color: {_dark_one};	
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        font: 800 9pt "Segoe UI";
    }}
    """

    def __init__(
        self,
        parent,
        tooltip,
        dark_one,
        text_foreground
    ):
        QLabel.__init__(self)

        # LABEL SETUP
        style = self.style_tooltip.format(
            _dark_one=dark_one,
            _text_foreground=text_foreground
        )
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(34)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)

        