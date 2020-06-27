import sys


from PyQt5.QtWidgets import QApplication
from temperature_converter import *


class MyApp(QtWidgets.QMainWindow, Ui_Temperature_Converter):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pushButton_Calculate.clicked.connect(self.convertEither)
        self.pushButton_clear_Celcius.clicked.connect(self.lineEdit_Celcius.clear)
        self.pushButton_clear_Farenheit.clicked.connect(self.lineEdit_Farenheit.clear)

    def convertEither(self):
        try:
            if self.lineEdit_Farenheit.text() == "" and self.lineEdit_Celcius.text() != "":
                f = (float(self.lineEdit_Celcius.text()) * (9 / 5) + 32)
                y=str(round(f,2))
                self.lineEdit_Farenheit.setText(y)
            elif self.lineEdit_Celcius.text() == "" and self.lineEdit_Farenheit.text() != "":
                c = (float(self.lineEdit_Farenheit.text()) - 32)*(5/9)
                a=str(round(c,2))
                self.lineEdit_Celcius.setText(a)
        except Exception:
            QtWidgets.QMessageBox.about(self, 'Error', 'Input can only be a number')


if __name__ == "__main__":
     app = QApplication(sys.argv)
     w = MyApp()
     w.show()
     sys.exit(app.exec_())
