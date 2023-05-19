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
