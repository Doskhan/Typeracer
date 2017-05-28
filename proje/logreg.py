import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from register import Register,Login
class LogReg(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def lr(self):


        self.single = QPushButton('Login', self)
        self.single.move(100, 10)
        self.single.clicked.connect(self.lg)

        self.multi = QPushButton('Register', self)
        self.multi.move(100, 60)
        self.multi.clicked.connect(self.reg)





        self.setGeometry(500, 300, 300, 300)
        self.setWindowTitle('Toggle button')
        self.show()

    def asd(self):
        print("asdasdcol")

    def lg(self):
        self.lg=Login()
        self.close()

    def reg(self):
        self.ex=Register()
        self.close()

    def ex(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = LogReg()
    sys.exit(app.exec_())
