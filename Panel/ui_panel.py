from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

F_WIDTH = 1200
F_HEIGHT = 700
TITLE = "这就是个临时的标题"
TITLE_SIZE = 32



class Ui_Form(QWidget):
    """UI界面管理类"""

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setObjectName("The Panel")
        self.setFixedSize(F_WIDTH, F_HEIGHT)
        self.setWindowOpacity(0.9)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.wid1 = QWidget(self)
        self.wid1.resize(F_WIDTH, F_HEIGHT)   
        self.setWindowOpacity(0.9)     
        self.wid1.setStyleSheet("background-color: rgba(225, 225, 255, 200);\
                                ")
        self.label1 = QLabel(self.wid1)
        self.label1.setText(TITLE)
        font1 = QFont()
        font1.setPointSize(32)
        font1.setFamily("黑体")
        self.label1.setFont(font1)
        x = (F_WIDTH - int(len(TITLE) * TITLE_SIZE / 0.75)) // 2
        print(x)
        self.label1.move(x, 70)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
