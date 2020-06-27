# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temperature_converter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Temperature_Converter(object):
    def setupUi(self, Temperature_Converter):
        Temperature_Converter.setObjectName("Temperature_Converter")
        Temperature_Converter.setWindowModality(QtCore.Qt.NonModal)
        Temperature_Converter.resize(467, 302)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Temperature_Converter.sizePolicy().hasHeightForWidth())
        Temperature_Converter.setSizePolicy(sizePolicy)
        Temperature_Converter.setMinimumSize(QtCore.QSize(467, 302))
        Temperature_Converter.setMaximumSize(QtCore.QSize(467, 302))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        Temperature_Converter.setFont(font)
        Temperature_Converter.setStyleSheet("QPushButton#pushButton_Calculate{\n"
"color:rgb(0, 85, 127);\n"
"border: 2px rgb(170, 170, 255);\n"
"border-radius: 10px;\n"
"padding:0 8px;\n"
"background:qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(32, 131, 246, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_clear_Celcius{\n"
"color:white;\n"
"border: 2px rgb(170, 170, 255);\n"
"border-radius: 10px;\n"
"padding:0 8px;\n"
"background:rgb(9,9,9);\n"
"}\n"
"\n"
"QPushButton#pushButton_clear_Farenheit{\n"
"color:white;\n"
"border: 2px rgb(170, 170, 255);\n"
"border-radius: 10px;\n"
"padding:0 8px;\n"
"background:rgb(9,9,9);\n"
"}\n"
"\n"
"\n"
"QLabel#label_Heading{\n"
"color:rgb(200, 201, 201);\n"
"}\n"
"QLineEdit#lineEdit_Celcius{\n"
"background-color:white;\n"
"border: 2px rgb(170, 170, 255);\n"
"border-radius: 10px;\n"
"padding:0 8px;\n"
"}\n"
"QLineEdit#lineEdit_Farenheit{\n"
"background-color:white;\n"
"border: 2px rgb(170, 170, 255);\n"
"border-radius: 10px;\n"
"padding:0 8px;\n"
"}\n"
"*\n"
"{\n"
"background:rgb(57, 93, 124);\n"
"}")
        self.widget = QtWidgets.QWidget(Temperature_Converter)
        self.widget.setGeometry(QtCore.QRect(0, 10, 473, 290))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_Heading = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Heading.sizePolicy().hasHeightForWidth())
        self.label_Heading.setSizePolicy(sizePolicy)
        self.label_Heading.setMinimumSize(QtCore.QSize(11, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(18)
        self.label_Heading.setFont(font)
        self.label_Heading.setAutoFillBackground(False)
        self.label_Heading.setObjectName("label_Heading")
        self.gridLayout.addWidget(self.label_Heading, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_Celcius = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_Celcius.setFont(font)
        self.label_Celcius.setTextFormat(QtCore.Qt.RichText)
        self.label_Celcius.setObjectName("label_Celcius")
        self.horizontalLayout_2.addWidget(self.label_Celcius)
        spacerItem4 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.lineEdit_Celcius = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Exotc350 Bd BT")
        font.setPointSize(16)
        self.lineEdit_Celcius.setFont(font)
        self.lineEdit_Celcius.setObjectName("lineEdit_Celcius")
        self.horizontalLayout_2.addWidget(self.lineEdit_Celcius)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButton_clear_Celcius = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.pushButton_clear_Celcius.setFont(font)
        self.pushButton_clear_Celcius.setObjectName("pushButton_clear_Celcius")
        self.horizontalLayout_2.addWidget(self.pushButton_clear_Celcius)
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.label_Farenheit = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(18)
        self.label_Farenheit.setFont(font)
        self.label_Farenheit.setObjectName("label_Farenheit")
        self.horizontalLayout_3.addWidget(self.label_Farenheit)
        spacerItem9 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.lineEdit_Farenheit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Exotc350 Bd BT")
        font.setPointSize(16)
        self.lineEdit_Farenheit.setFont(font)
        self.lineEdit_Farenheit.setObjectName("lineEdit_Farenheit")
        self.horizontalLayout_3.addWidget(self.lineEdit_Farenheit)
        spacerItem10 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.pushButton_clear_Farenheit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.pushButton_clear_Farenheit.setFont(font)
        self.pushButton_clear_Farenheit.setObjectName("pushButton_clear_Farenheit")
        self.horizontalLayout_3.addWidget(self.pushButton_clear_Farenheit)
        spacerItem11 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.pushButton_Calculate = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Calculate.setFont(font)
        self.pushButton_Calculate.setObjectName("pushButton_Calculate")
        self.horizontalLayout_4.addWidget(self.pushButton_Calculate)
        spacerItem14 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 7, 0, 1, 1)

        self.retranslateUi(Temperature_Converter)
        QtCore.QMetaObject.connectSlotsByName(Temperature_Converter)
        Temperature_Converter.setTabOrder(self.lineEdit_Celcius, self.pushButton_Calculate)
        Temperature_Converter.setTabOrder(self.pushButton_Calculate, self.pushButton_clear_Celcius)
        Temperature_Converter.setTabOrder(self.pushButton_clear_Celcius, self.lineEdit_Farenheit)
        Temperature_Converter.setTabOrder(self.lineEdit_Farenheit, self.pushButton_clear_Farenheit)

    def retranslateUi(self, Temperature_Converter):
        _translate = QtCore.QCoreApplication.translate
        Temperature_Converter.setWindowTitle(_translate("Temperature_Converter", "Form"))
        self.label_Heading.setText(_translate("Temperature_Converter", "TEMPERATURE CONVERTER"))
        self.label_Celcius.setText(_translate("Temperature_Converter", "Celcius"))
        self.pushButton_clear_Celcius.setText(_translate("Temperature_Converter", "Clear"))
        self.label_Farenheit.setText(_translate("Temperature_Converter", "Farenheit"))
        self.pushButton_clear_Farenheit.setText(_translate("Temperature_Converter", "Clear"))
        self.pushButton_Calculate.setText(_translate("Temperature_Converter", "CALCULATE"))
