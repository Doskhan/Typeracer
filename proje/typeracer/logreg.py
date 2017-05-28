import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from register import Register
from start import Login
class LogReg(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()



    def initUI(self):

        palette= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("wel1.jpg")))
        self.setPalette(palette)

        self.single = QPushButton('Login', self)
        self.single.move(60, 250)
        self.single.resize(100,50)
        self.single.setStyleSheet('QPushButton {background-color:white;font-size:20px;border-radius:5px;width:50px;}')
        self.single.clicked.connect(self.lg)

        self.multi = QPushButton('Register', self)
        self.multi.move(270, 250)
        self.multi.resize(100,50)
        self.multi.setStyleSheet('QPushButton {background-color:white;font-size:20px;border-radius:5px;width:50px;}')

        self.multi.clicked.connect(self.reg)





        self.setGeometry(450, 150, 410, 310)
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
