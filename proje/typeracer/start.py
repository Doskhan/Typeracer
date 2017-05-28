import requests
import sys
import sqlite3
conn = sqlite3.connect('us.db')
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import Typeracer
from admin import Admin

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setStyleSheet('QPushButton{background-color:pink;border-radius:5px;font-size:20px;}')
        self.single = QPushButton('Single player', self)

        self.single.clicked.connect(self.sing)

        self.multi = QPushButton('Multiplayer', self)

        self.multi.clicked.connect(self.mult)

        self.set = QPushButton('Profile', self)

        self.set.clicked.connect(self.asd)

        self.exit = QPushButton('Exit', self)

        self.exit.clicked.connect(self.ex)

        grid = QGridLayout()
        grid.addWidget(self.single, 0, 0)
        grid.addWidget(self.multi, 2, 0)
        grid.addWidget(self.set,3,0)
        grid.addWidget(self.exit, 4, 0)
        self.setLayout(grid)


        global login
        self.setGeometry(500, 300, 300, 300)
        self.setWindowTitle('%s'%(login))
        self.show()

    def asd(self):
        if login=="Admin":
            self.ad=Admin()
        else:
            self.ad=Profile()

    def mult(self):
        self.lg=Typeracer()
        self.close()

    def sing(self):
        self.ex=Typeracer()
        self.close()

    def ex(self):
        self.close()
class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.Login()


    def Login(self):
        palette= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("wall.png")))
        self.setPalette(palette)
        self.setStyleSheet('QLabel{font-size:20px;color:white}')

        self.lbllog=QLabel("Login: ",self)
        self.lblpas=QLabel("Password: ",self)
        self.empty = QLabel(self)
        self.log = QLineEdit()
        self.pas = QLineEdit()
        self.btn = QPushButton('Login', self)
        self.btn.resize(self.btn.sizeHint())

        grid = QGridLayout()
        grid.addWidget(self.lbllog, 0, 0)
        grid.addWidget(self.log, 1, 0)
        grid.addWidget(self.lblpas,2,0)
        grid.addWidget(self.pas, 3, 0)
        grid.addWidget(self.empty, 4, 0)
        grid.addWidget(self.btn,5,0)


        self.setLayout(grid)
        self.btn.clicked.connect(self.asd)
        self.setGeometry(450, 150, 200, 150)
        self.setWindowTitle('Login')
        self.show()
    def asd(self):
        c = conn.cursor()
        c.execute("SELECT * FROM last WHERE email='%s' AND password='%s' " % (str(self.log.text()), str(self.pas.text())))
        a = c.fetchall()
        print(a)
        if len(a)>0:
            global login
            login=a[0][1]
            self.setStyleSheet('QMessageBox{font-size:20px;color:black}')
            QMessageBox.information(self, "WELCOME", "%s , you are Welcome" %(a[0][1]))
            self.game=Example()
            self.close()

        else:
            QMessageBox.information(self,"ERROR", "INVALID EMAIL OR PASSWORD! Please try again!")
            self.log.setText("")
            self.pas.setText("")
        conn.commit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
