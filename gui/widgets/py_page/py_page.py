from qt_core import *

from gui.core.functions import *

class PyPage(QWidget):
    clicked = Signal(object)
    released = Signal(object)
    def __init__(self    ):
        super().__init__()




    def btn_clicked(self):
        self.clicked.emit(self.menu)
    
    def btn_released(self):
        self.released.emit(self.menu)