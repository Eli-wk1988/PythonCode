from uiform_ui import *
import sys
from LoClk import *

def plus():
    print("2 + 3 = 5")

class UIMain(Ui_Form):

    def __init__(self, long = None):
        self.long = long
        pass

    def setupUi(self, Form):
        super().setupUi(Form)
        self.pushButton = LoClick("测试按钮",Form, long = self.long)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 100, 150, 51))
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.sinout.connect(self.btn1)


    def btn1(self, int1):
        if int1 == 0:
            print(self.pushButton.text() + "被按下")
        elif int1 == 1:
            print(self.pushButton.text() + "未设置点动函数")
        elif int1 == 2:
            print(self.pushButton.text() + "点动函数运行中")
        elif int1 == 3:
            print(self.pushButton.text() + "未设置长按函数")
        elif int1 == 4:
            print(self.pushButton.text() + "长按函数运行中")
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    ui = UIMain()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())