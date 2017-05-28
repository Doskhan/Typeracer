import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import socket
import threading
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import pymysql
pymysql.install_as_MySQLdb()


class Userrs(QWidget):
    def __init__(self):

        super().__init__()
        self.db = pymysql.connect("localhost","root","","bauka" )
        self.c = self.db.cursor()
        self.c.execute("SELECT * FROM python")
        self.users = self.c.fetchall()
        self.len = len(self.users)
        self.user()

    def user(self):
        col = ['username', 'password']
        row = [[QLineEdit() for i in range(5)] for j in range(self.len+1)]
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.page = QLabel("USERS", self)
        self.grid.addWidget(self.page, 0, 2)
        for i in range(len(self.users)):
            for j in range(len(self.users[i])):
                row[i][j].setText("%s"%self.users[i][j])
                if j == 0:
                    row[i][j].setReadOnly(True)
                else:
                    row[i][j].setObjectName(col[j-1]+str(self.users[i][0]))
                self.grid.addWidget(row[i][j], i+1, j)
            row[i][3] = QPushButton("Update", self)
            row[i][3].setObjectName(str(self.users[i][0]))
            self.grid.addWidget(row[i][3], i+1, j+1)
            row[i][4] = QPushButton("Delete", self)
            row[i][4].setObjectName(str(self.users[i][0]))
            self.grid.addWidget(row[i][4], i+1, j+2)
            row[i][3].clicked.connect(self.update)
            row[i][4].clicked.connect(self.delete)
        row[self.len][0] = QLabel("Fill the blanks for New user", self)
        row[self.len][1].setObjectName("username")
        row[self.len][2].setObjectName("password")
        row[self.len][3] = QPushButton("Insert", self)
        row[self.len][3].clicked.connect(self.insert)
        row[self.len][4] = QPushButton('Main page', self)
        row[self.len][4].clicked.connect(self.mainmenu)
        for i in range(5):
            self.grid.addWidget(row[self.len][i], self.len+1, i)
        self.move(400, 100)
        self.setWindowTitle('Typeracer')
        self.show()
    def update(self):
        sender=self.sender()
        self.id = sender.objectName()
        # q = "UPDATE python SET 'username' = '' 'password' = '%s' WHERE id = '%s'"%(username, password, self.id)
        username = self.findChild(QObject, 'username%s'%self.id).property('text')
        password = self.findChild(QObject, 'password%s'%self.id).property('text')
        q = "UPDATE python set username = '%s',password = '%s' where id = '%s'"%(username, password, self.id)
        self.c.execute(q)
        self.db.commit()
        self.NEW = Userrs()
        self.close()
    def delete(self):
        sender=self.sender()
        self.id = sender.objectName()
        self.db = pymysql.connect("localhost","root","","bauka")
        self.c = self.db.cursor()
        self.c.execute("DELETE from python WHERE id = '%s'"%self.id)
        self.db.commit()
        self.show()
        self.NEW = Userrs()
        self.close()
    def insert(self):
        self.db = pymysql.connect("localhost","root","","bauka")
        self.c = self.db.cursor()
        username = self.findChild(QObject, 'username').property('text')
        password = self.findChild(QObject, 'password').property('text')
        self.c.execute("INSERT into python (username, password) VALUES ('%s', '%s')"%(username, password))
        self.db.commit()
        self.NEW = Userrs()
        self.close()
    def mainmenu(self):
        self.ex = Example()
        self.close()



class NewText(QWidget):
    def __init__(self):
        super().__init__()
        self.addTextUI()

    def addTextUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        name = QLabel('Title', self)
        diff = QLabel('Difficulty', self)
        text = QLabel('Text', self)
        self.name_line = QLineEdit(self)
        self.diff_line = QComboBox(self)
        self.diff_line.addItem("Easy")
        self.diff_line.addItem("Normal")
        self.diff_line.addItem("Hard")
        self.text_line = QTextEdit(self)
        submit = QPushButton('Submit', self)
        self.grid.addWidget(name, 0, 0)
        self.grid.addWidget(diff, 1, 0)
        self.grid.addWidget(text, 2, 0)
        self.grid.addWidget(self.name_line, 0, 1)
        self.grid.addWidget(self.diff_line, 1, 1)
        self.grid.addWidget(self.text_line, 2, 1, 5, 5)
        self.grid.addWidget(submit, 7, 5)
        submit.clicked.connect(self.submit)
        self.move(400, 100)
        self.setWindowTitle('Typeracer')
        self.show()
    def submit(self):
        new_file = open("texts/%s%s.txt"%(self.name_line.text(), self.diff_line.currentText()[0]), 'w')
        new_file.write("%s"%(self.text_line.toPlainText()))
        new_file.close()
        self.file = File()
        self.close()

class File(QWidget):
    def __init__(self):
        super().__init__()
        self.textUI()

    def textUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        a = len(os.listdir("texts"))
        b = [(QLineEdit(), QPushButton('Delete text')) for i in range(a)]
        c = os.listdir("texts")
        for i in range(a):
            b[i][0].setText(c[i][:-4])
            b[i][0].setReadOnly(True)
            b[i][1].setObjectName('%s'%c[i])
            b[i][1].clicked.connect(self.delete)
            self.grid.addWidget(b[i][0], i, 0)
            self.grid.addWidget(b[i][1], i, 1)
        self.addtext = QPushButton('Add text', self)
        self.main = QPushButton('Main page', self)
        self.grid.addWidget(self.main, a, 0)
        self.grid.addWidget(self.addtext, a, 1)
        self.addtext.clicked.connect(self.addText)
        self.main.clicked.connect(self.main_page)
        self.setGeometry(400, 100, 300, 0)
        self.setWindowTitle('Typeracer')
        self.show()

    def delete(self):
        sender=self.sender()
        file_name = sender.objectName()
        os.remove("texts/%s"%file_name)
        self.new = File()
        self.close()

    def main_page(self):
        self.menu = Example()
        self.close()

    def addText(self):
        self.adT = NewText()
        self.close()





class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.page = QLabel("ADMIN PAGE", self)
        self.listOfText = QPushButton('List of texts', self)
        self.users = QPushButton('Users', self)
        self.users.clicked.connect(self.userss)
        self.listOfText.clicked.connect(self.addFile)
        self.grid.addWidget(self.page, 0, 0)
        self.grid.addWidget(self.users, 1, 0)
        self.grid.addWidget(self.listOfText, 2, 0)
        self.setGeometry(400, 100, 300, 0)
        self.setWindowTitle('Typeracer')
        self.show()

    def userss(self):
        self.user = Userrs()
        self.close()

    def addFile(self):
        self.file = File()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
