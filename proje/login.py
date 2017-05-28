import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
from o import
conn = sqlite3.connect('us.db')


class login(QWidget):

    def __init__(self):
        super().__init__()
        self.login()


    def login(self):
        self.lbl = Qlabel("Login:",self)
        self.lbl1 = Qlabel("Password:",self)
        self.lbl2 = Qlabel(self)
        self.log = QLineEdit()
        self.pas = QLineEdit()
        self.btn = QPushButton('Login', self)
        self.btn.resize(self.btn.sizeHint())

        grid = QGridLayout()
        grid.addWidget(self.lbl, 0, 0)
        grid.addWidget(self.log,1,0)
        grid.addWidget(self.lbl1,2,0)
        grid.addWidget(self.lbl1,4,0)
        grid.addWidget(self.pas,3,0)
        grid.addWidget(self.btn,5,0)



        self.setLayout(grid)
        self.btn.clicked.connect(self.asd)
        self.setGeometry(450, 150, 200, 150)
        self.setWindowTitle('Registration')
        self.show()
    def asd(self):
        c = conn.cursor()
        c.execute("SELECT * FROM last WHERE email='%s' AND password='%s' " % (str(self.log.text()), str(self.pas.text())))
        a = c.fetchall()
        print(a)
        if len(a)>0:
            QMessageBox.information(self, "WELCOME", "%s, you are Welcome" %(a[0][2], a[0][1]))
            self.text=texts()

        else:
            QMessageBox.information(self,"ERROR", "INVALID EMAIL OR PASSWORD! Please try again!")
            self.log.setText("")
            self.pas.setText("")
        conn.commit()
        conn.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    g = login()
    sys.exit(app.exec_())
