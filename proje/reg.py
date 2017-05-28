import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql
pymysql.install_as_MySQLdb()

db=pymysql.connect("localhost","root","","bauka")

c=db.cursor()




class login(QWidget):

    def __init__(self):
        super().__init__()
        self.login()


    def login(self):

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
        self.btn.clicked.connect(self.Register)
        self.setGeometry(450, 150, 200, 150)
        self.setWindowTitle('Registration')
        self.show()
    def Register(self):

        name = self.name.text()
        surname = self.surname.text()
        login = self.login.text()
        password = self.password.text()
                # self.c.execute("INSERT into python (username, password) VALUES ('%s', '%s')"%(username, password))

        c.execute("INSERT into python (username,password) VALUES ('%s','%s')"%(str(login),str(password)))

        db.close

if __name__ == '__main__':

    app = QApplication(sys.argv)
    g = login()
    sys.exit(app.exec_())
