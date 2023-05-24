### 长按按钮管理类
```
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoClick(QPushButton):
    """含点动功能和长按功能的按钮管理类"""
    sinout = Signal(int)    # 0:按下, 1:未设置点动 2:点动 3:未设置长按 4:长按

    def __init__(
                    self, 
                    text:str,               # 按钮文本
                    parent,                 # 按钮父类
                    timeout1:int = 500,     # 设定长按门槛时间(ms)
                    jump = None,            # 设定点动函数
                    long = None             # 设定长按函数
                    ):
        super().__init__(text, parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.LoClk)
        self.timeoutflag = False      # 进入长按标志位
        self.timeout1 = timeout1      
        self.jump = jump
        self.long = long

    def mousePressEvent(self, e) :
        self.timer.start(self.timeout1)
        self.sinout.emit(0)

    def mouseReleaseEvent(self, e) :
        if not self.timeoutflag:
            if self.jump == None:
                self.sinout.emit(1)
            else:
                self.sinout.emit(2)
        self.timer.stop()
        self.timeoutflag = False

    def LoClk(self):
        if self.long == None:
            self.sinout.emit(3)
        else:
            self.sinout.emit(4)
        self.timeoutflag = True
        self.timer.stop()
```

### 测试代码
```
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
```
### UI代码
```
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiform.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        #self.pushButton = QPushButton(Form)
        #self.pushButton.setObjectName(u"pushButton")
        #self.pushButton.setGeometry(QRect(140, 100, 150, 51))
        #font = QFont()
        #font.setPointSize(12)
        #self.pushButton.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        #self.pushButton.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u6309\u94ae", None))
    # retranslateUi
```
