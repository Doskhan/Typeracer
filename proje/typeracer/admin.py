import sys
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Admin(QWidget):

	def __init__(self):
		self.conn = sqlite3.connect('us.db')
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300,750,250)
		c = self.conn.cursor()
		c.execute("SELECT * FROM last")
		self.grid = QGridLayout()
		self.setLayout(self.grid)
		list=c.fetchall()

		list.append(["","","",""])
		row=len(list)
		col=len(list[0])
		self.le = [[QLineEdit(self) for j in range(col)] for i in range(row)]
		self.btn = [[QPushButton(self) for j in range(2)] for i in range(row-1)]
		for i in range(row):
			for j in range(col):
				self.le[i][j].setReadOnly(False if i==row-1 else True)
				self.le[i][j].setText(str(list[i][j]))
				self.le[i][j].setFixedWidth(20 if j==0 else 150 if j==3 else 100)
				self.le[i][j].setFixedHeight(25)
				self.grid.addWidget(self.le[i][j], i, j)

		for i in range(row-1):
			self.btn[i][0].setText("Edit")
			self.btn[i][0].setFixedHeight(27)
			self.btn[i][0].setObjectName(str(i))
			self.btn[i][0].clicked.connect(self.buttonEditClicked)

			self.btn[i][1].setText("Delete")
			self.btn[i][1].setFixedHeight(27)
			self.btn[i][1].setObjectName(str(i))
			self.btn[i][1].clicked.connect(self.buttonDeleteClicked)
			self.grid.addWidget(self.btn[i][0], i, col)
			self.grid.addWidget(self.btn[i][1], i, col+1)

		self.btnInsert=QPushButton(self)
		self.btnInsert.setText("Insert")
		self.btnInsert.setFixedHeight(27)
		self.btnInsert.setObjectName(str(row-1))
		self.btnInsert.clicked.connect(self.buttonInsertClicked)
		self.grid.addWidget(self.btnInsert, row-1, col)

		self.conn.close()
		self.setWindowTitle('SQL')
		self.show()

	def buttonEditClicked(self):
		self.conn = sqlite3.connect('us.db')
		c = self.conn.cursor()
		sender = self.sender()
		id = int(sender.objectName())

		value = not self.le[id][3].isReadOnly()
		for i in range(1,4):
			self.le[id][i].setReadOnly(value)
		self.btn[id][0].setText("Edit" if value == True else "Save")
		name = self.le[id][1].text()
		email= self.le[id][2].text()
		password = self.le[id][3].text()
		c.execute("UPDATE last SET name=\'"+ name +"\', email=\'" + email +"\' , password=\'" + password +"\' WHERE id=\'" + str(id) + "\'")
		self.conn.commit()
		


	def buttonDeleteClicked(self):
		self.conn = sqlite3.connect('us.db')
		c = self.conn.cursor()
		sender = self.sender()
		id = int(sender.objectName())
		name = self.le[id][2].text()
		c.execute("DELETE FROM last WHERE email='%s'" %name)
		self.conn.commit()
		self.new=Admin()
		self.close()


	def buttonInsertClicked(self):
		self.conn = sqlite3.connect('us.db')
		c = self.conn.cursor()
		a = self.conn.cursor()
		sender = self.sender()
		id = int(sender.objectName())
		name = self.le[id][1].text()
		email = self.le[id][2].text()
		password = self.le[id][3].text()

		if name!="" and email!="" and password!="":
			a.execute("INSERT INTO last (name, email,password) VALUES(\'" + name +"\', \'" + email +"\',\'" + password +"\')")
		c.execute("SELECT * FROM last")

		self.conn.commit()
		self.new=Admin()
		self.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Admin()
	sys.exit(app.exec_())
