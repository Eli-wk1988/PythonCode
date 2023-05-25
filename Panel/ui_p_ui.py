# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_p.ui'
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
        Form.resize(1200, 700)
        Form.setAutoFillBackground(False)
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(-1, -1, 1201, 701))
        self.widget_3.setStyleSheet(u"border-radius:100px;")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(365, 70, 470, 48))
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgba(0, 85, 255, 122);")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1110, 40, 32, 32))
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 0, 0, 255);\n"
"border-radius:16px;")
        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1070, 40, 32, 32))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius:16px;")
        self.pushButton_13 = QPushButton(self.widget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(525, 580, 150, 32))
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(24)
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setStyleSheet(u"background-color: rgba(255, 0, 0, 122);\n"
"border-radius: 10px;")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(274, 140, 651, 241))
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 648, 241))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setFrameShape(QFrame.Panel)
        self.label_7.setFrameShadow(QFrame.Sunken)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setFrameShape(QFrame.Panel)
        self.label_13.setFrameShadow(QFrame.Sunken)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 5, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setFrameShape(QFrame.Panel)
        self.label_3.setFrameShadow(QFrame.Sunken)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setFrameShape(QFrame.Panel)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setFrameShape(QFrame.Panel)
        self.label_9.setFrameShadow(QFrame.Sunken)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setFrameShape(QFrame.Panel)
        self.label_11.setFrameShadow(QFrame.Sunken)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 3, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout.addWidget(self.label_15, 5, 2, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setFrameShape(QFrame.Panel)
        self.label_14.setFrameShadow(QFrame.Sunken)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 5, 3, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(160, 400, 881, 151))
        self.gridLayoutWidget_2 = QWidget(self.widget_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(-1, 9, 881, 139))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"background-color: rgba(255, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_8, 2, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"background-color: rgba(255, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"background-color: rgba(255, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setStyleSheet(u"background-color: rgba(127, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_9, 1, 3, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font2)
        self.pushButton_11.setStyleSheet(u"background-color: rgba(127, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_11, 1, 4, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"background-color: rgba(0, 255, 255, 50);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setStyleSheet(u"background-color: rgba(127, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_12, 2, 4, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setStyleSheet(u"background-color: rgba(127, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_10, 2, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: rgba(0, 255, 255, 50);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"background-color: rgba(255, 255, 127, 122);\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        font3 = QFont()
        font3.setFamily(u"\u9ed1\u4f53")
        font3.setPointSize(16)
        self.label_18.setFont(font3)
        self.label_18.setFrameShape(QFrame.StyledPanel)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_18, 0, 3, 1, 2)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setFrameShape(QFrame.Box)
        self.label_16.setFrameShadow(QFrame.Raised)
        self.label_16.setLineWidth(5)
        self.label_16.setMidLineWidth(1)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setFrameShape(QFrame.StyledPanel)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 0, 1, 1, 2)

        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_13.raise_()
        self.widget_2.raise_()
        self.widget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6446\u52a8\u7f38\u8bd5\u9a8c\u4e0a\u4f4d\u63a7\u5236\u7cfb\u7edf", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"_", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u4e2d", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u9501\u5b9a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u672a\u8fde\u63a5", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6b62\u52a8\u5668\u9501\u5b9a", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"99.99\u00b0", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6b62\u52a8\u5668\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u72b6\u6001\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u673a\u68b0\u9501\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u6a21\u5f0f\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u89d2\u5ea6\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u4e2d", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u538b\u529b\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"20.00MPa", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u6b62\u52a8\u5668\u89e3\u9501", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5929\u7ebf\u5c55\u5f00", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u5929\u7ebf\u64a4\u6536", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u673a\u68b0\u9501\u89e3\u9501", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"\u5929\u7ebf\u70b9\u52a8\u5c55\u5f00", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u8054\u52a8\u64a4\u6536", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"\u5929\u7ebf\u70b9\u52a8\u64a4\u6536", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u673a\u68b0\u9501\u9501\u5b9a", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u8054\u52a8\u5c55\u5f00", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u6b62\u52a8\u5668\u9501\u5b9a", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"- \u624b\u52a8\u64cd\u4f5c -", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"- \u8054\u52a8\u64cd\u4f5c -", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"- \u5206\u52a8\u64cd\u4f5c -", None))
    # retranslateUi

