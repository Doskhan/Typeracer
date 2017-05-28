import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from register import Register,Login
from main import Typeracer
from lgreg import LogReg
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        self.single = QPushButton('Single player', self)
        self.single.move(100, 10)
        self.single.clicked.connect(self.sing)

        self.multi = QPushButton('Multiplayer', self)
        self.multi.move(100, 60)
        self.multi.clicked.connect(self.mult)

        self.set = QPushButton('Settings', self)
        self.set.move(100, 110)
        self.set.clicked.connect(self.asd)

        self.exit = QPushButton('Exit', self)
        self.exit.move(100, 160)
        self.exit.clicked.connect(self.ex)



        self.setGeometry(500, 300, 300, 300)
        self.setWindowTitle('Toggle button')
        self.show()

    def asd(self):
        print("asdasdcol")

    def mult(self):
        self.lg=LogReg()
        self.close()

    def sing(self):
        self.ex=Typeracer()
        self.close()

    def ex(self):
        self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
