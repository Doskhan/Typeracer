import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
from main import Typeracer
conn = sqlite3.connect('us.db')




class Register(QWidget):

    def __init__(self):
        super().__init__()
        self.Register()


    def Register(self):

        self.name = QLineEdit()
        self.surname = QLineEdit()
        self.login = QLineEdit()
        self.password = QLineEdit()
        self.btn = QPushButton('Register', self)
        self.btn.resize(self.btn.sizeHint())

        grid = QGridLayout()
        grid.addWidget(self.name, 1, 0)
        grid.addWidget(self.surname,2,0)
        grid.addWidget(self.login,3,0)
        grid.addWidget(self.password,4,0)
        grid.addWidget(self.btn,5,0)


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
        c.execute("INSERT INTO qwerty (NAME,SURNAME,EMAIL,PASSWORD,TYPE) VALUES ('%s','%s','%s','%s',0)"%(str(name),str(surname),str(login),str(password)))
        conn.commit()


        self.ex = Login()
        self.close()
class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.Login()


    def Login(self):
        self.log = QLineEdit()
        self.pas = QLineEdit()
        self.btn = QPushButton('Login', self)
        self.btn.resize(self.btn.sizeHint())

        grid = QGridLayout()
        grid.addWidget(self.log, 0, 0)
        grid.addWidget(self.pas,1,0)
        grid.addWidget(self.btn,2,0)


        self.setLayout(grid)
        self.btn.clicked.connect(self.asd)
        self.setGeometry(450, 150, 200, 150)
        self.setWindowTitle('Login')
        self.show()
    def asd(self):
        c = conn.cursor()
        c.execute("SELECT * FROM qwerty WHERE email='%s' AND password='%s' " % (str(self.log.text()), str(self.pas.text())))
        a = c.fetchall()
        print(a)
        if len(a)>0:
            QMessageBox.information(self, "WELCOME", "%s %s, you are Welcome" %(a[0][2], a[0][1]))
            self.game=Typeracer()
            self.close()

        else:
            QMessageBox.information(self,"ERROR", "INVALID EMAIL OR PASSWORD! Please try again!")
            self.log.setText("")
            self.pas.setText("")
        conn.commit()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    g = Register()
    sys.exit(app.exec_())
