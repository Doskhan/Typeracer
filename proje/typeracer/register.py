import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
conn = sqlite3.connect('us.db')
from main import Typeracer
from start import Example,Login




class Register(QWidget):

    def __init__(self):
        super().__init__()
        self.Register()


    def Register(self):
        palette= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("wall.png")))
        self.setPalette(palette)
        self.setStyleSheet('QLabel{font-size:20px;color:white}')
        self.lblname=QLabel("Name: ",self)
        self.lblsur=QLabel("Surname: ",self)
        self.lbllog=QLabel("Login: ",self)
        self.lblpas=QLabel("Password: ",self)
        self.lblempty=QLabel(self)

        self.name = QLineEdit()
        self.surname = QLineEdit()
        self.login = QLineEdit()
        self.password = QLineEdit()
        self.btn = QPushButton('Register', self)
        self.btn.resize(self.btn.sizeHint())

        grid = QGridLayout()
        grid.addWidget(self.name, 2, 0)
        grid.addWidget(self.lblname, 1, 0)
        grid.addWidget(self.lblsur, 3, 0)
        grid.addWidget(self.lblpas, 7, 0)
        grid.addWidget(self.lbllog, 5, 0)
        grid.addWidget(self.surname,4,0)
        grid.addWidget(self.login,6,0)
        grid.addWidget(self.password,8,0)
        grid.addWidget(self.lblempty,9,0)
        grid.addWidget(self.btn,10,0)


        self.setLayout(grid)
        self.btn.clicked.connect(self.reg)
        self.setGeometry(450, 150, 200, 150)
        self.setWindowTitle('Registration')
        self.show()
    def reg(self):
        c = conn.cursor()

        name = self.name.text()
        surname = self.surname.text()
        login = self.login.text()
        password = self.password.text()
        c.execute("INSERT INTO last (NAME,EMAIL,PASSWORD) VALUES ('%s','%s','%s')"%(str(name),str(login),str(password)))
        conn.commit()


        self.ex = Login()
        self.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    g = Register()
    sys.exit(app.exec_())
