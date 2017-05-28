#KEY EVENT
import requests
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import (QWidget, QLabel,
	QComboBox, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QMessageBox, QMainWindow)
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
import random
class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.wrongs=0
		self.symbols=[")","!","@","#","$","%","^","&","*","("]
		self.big=0
		self.onelin=0
		self.alltext=1
		self.big1=0
		self.probel=0
		self.pixmapNull = QPixmap("")
		self.pixmapGoodLuck = QPixmap("goodluck.png")
		self.pixmapCorrect = QPixmap("correct.png").scaled(50,50)
		self.pixmapIncorrect = QPixmap("incorrect.png").scaled(50,50)
		pixmapCar = QPixmap("car.png").scaled(50,70)
		pixmapRoad= QPixmap("line.png").scaled(700, 140)
		self.length=['My','name','is','Shakhmar.','I','am','from','Kentau.','I','am','student','of','Suleyman','Demirel','University.']
		self.step=(700-50)//len(self.length)
		self.laststep=(700-50)%len(self.length)
		self.lbl8=QLabel(self)
		self.lbl8.setStyleSheet('QLabel {background: white;}')
		self.lbl8.resize(700, 60)
		self.lbl8.move(250, 50)
		self.lbl9=QLabel(self)

		self.lbl9.setStyleSheet('QLabel {background: white;}')
		self.lbl9.resize(700, 8)
		self.lbl9.move(250, 110)
		self.lbl9.setPixmap(pixmapRoad)
		self.carplace=250
		self.speedplace=210
		self.lbl10=QLabel(self)
		self.lbl10.setStyleSheet('QLabel {background: white;}')
		self.lbl10.resize(50,60)
		self.lbl10.move(self.carplace,50)
		self.lbl10.setPixmap(pixmapCar)
		self.lbl23=QLabel("Good luck!",self)
		self.resize(10, 20)
		self.lbl23.move(300,50)
		self.lbl23.setStyleSheet('QLabel {color:blue;}')
		self.currenttext=''
		self.numwrongs=0
		for i in range(len(self.length)):
			self.currenttext+=self.length[i]
			self.currenttext+=" "
		self.lbl6 = QLabel("You", self)
		self.lbl11=QLabel("Shakhmar Sarsenbay", self)
		self.lbl12=QLabel("The average: 000 wpm", self)
		self.lbl22=QLabel("Your wrongs: 000", self)
		self.lbl2 = QLabel("000 wpm", self)
		self.lbl3 = QLabel("The best: 000 wpm", self)
		self.lbl6.setStyleSheet('QLabel {background:white;font-size:20px;font-family:bold}')
		self.lbl6.resize(40,20)
		self.lbl6.move(self.speedplace, 70)
		self.lbl2.resize(140,30)
		self.lbl2.setStyleSheet('QLabel {background:white;font-size:30px;}')
		self.lbl2.move(950, 88)
		self.lbl11.move(1050,10)
		self.lbl11.resize(400,30)
		self.lbl11.setStyleSheet('QLabel {background:#FFD700;font-size:30px;}')
		self.lbl12.move(1100,170)
		self.lbl12.resize(220,30)
		self.lbl12.setStyleSheet('QLabel {background:#F0E68C;font-size:20px;}')
		self.lbl22.move(1100,130)
		self.lbl22.resize(170,30)
		self.lbl22.setStyleSheet('QLabel {background:#F0E68C;font-size:20px;}')
		self.lbl3.move(1100, 210)
		self.lbl3.resize(200,30)
		self.lbl3.setStyleSheet('QLabel {background:#F0E68C;font-size:20px;}')
		self.lbl21=QLabel("Press here and start typing--->", self)
		self.lbl21.move(130, 570)
		self.lbl21.resize(280,30)
		self.lbl21.setStyleSheet('QLabel {background:white;font-size:20px;}')
		self.lbl1 = QLabel(self.currenttext, self)
		self.lbl1.setStyleSheet('QLabel {background: white; font-size:20px;;}')
		self.lbl1.move(200, 200)
		self.lbl1.resize(800, 300)
		self.lbl15=QLabel("Your speed: 000 wpm", self)
		self.lbl15.move(1100,90)
		self.lbl15.resize(220,30)
		self.lbl15.setStyleSheet('QLabel {background:#F0E68C;font-size:20px;}')
		self.le =QLineEdit('',self)
		self.le.move(400, 550)
		self.le.resize(400, 60)

		self.average=0
		self.attempts=0
		self.bestofbest=0
		self.combo = QComboBox(self)
		self.combo.addItem("show full text")
		self.combo.addItem("show one line of text")
		self.combo.setStyleSheet('QComboBox {font-size:15px;}')
		self.combo.activated[str]
		self.combo.move(800, 510)
		self.combo.resize(200, 30)
		self.le.setStyleSheet('QLineEdit {background: white; font-size:30px;}')
		self.btn = QPushButton('Restart', self)
		self.btn.move(500, 620)
		self.btn.resize(200, 50)
		self.btn.setStyleSheet('QPushButton {background:white;font-family:bold; font-size:30px;}')
		self.btn.clicked
		self.timer = QBasicTimer()
		self.time=0
		self.timerstar=0
		self.enteredletters=0
		self.thebest=0
		self.setStyleSheet('QMainWindow {background:#00FFFF;}')
		self.setGeometry(0, 0, 1500, 600)
		self.setWindowTitle('Type Racer')
		self.show()
def keyPressEvent(self, e):
	if e.key()==32 and self.probel<len(self.length):
		if self.le.text()==self.length[self.probel]:
			if self.probel+1==len(self.length):
				self.enteredletters+=len(self.length[self.probel])
			else:
				self.enteredletters+=(len(self.length[self.probel])+1)
			self.probel+=1
			if self.probel==len(self.length):
				self.carplace=self.carplace+self.step+self.laststep
				self.speedplace=self.carplace-40
			else:
				self.carplace+=self.step
				self.speedplace=self.carplace-40
			self.le.setText('')
			self.lbl10.move(self.carplace,50)
			self.lbl6.move(self.speedplace, 70)
			self.moveSound = "gold.wav"
			QSound.play(self.moveSound)
			if self.probel==len(self.length):
				self.timer.stop()
				if self.attempts==0:
					self.bestofbest=self.wpm
					self.lbl3.setText("The best: "+str(self.bestofbest)+" wpm")
				else:
					if self.wpm>self.bestofbest:
						self.bestofbest=self.wpm
						self.lbl3.setText("The best: "+str(self.bestofbest)+" wpm")
				self.attempts+=1
				self.average+=self.wpm
				avv=self.average//self.attempts
				self.lbl22.setText("Your wrongs: "+str(self.numwrongs))
				self.lbl15.setText("Your speed: "+str(self.wpm)+" wpm")
				self.lbl12.setText("The average: "+str(avv)+" wpm")
				print("It is over!")
		else:
			if self.le.text()!="":
				self.le.setText(self.le.text()+" ")
	def doAction(self):
		self.timer.stop()
		self.timerstar=0
		self.time=0
		self.wrongs=0
		self.enteredletters=0
		self.probel=0
		self.carplace=250
		self.speedplace=210
		self.lbl2.setText("000 wpm")
		self.lbl21.setText("Type here-->")
		self.lbl21.move(230, 570)
		self.lbl21.resize(170,30)
		self.lbl22.setText("Your wrongs: 000")
		self.lbl15.setText("Your speed: 000 wpm")
		self.lbl21.setStyleSheet('QLabel {background:white;font-size:30px;}')
		self.le.setText('')
		self.le.setStyleSheet('QLineEdit {background: white; font-size:30px;}')
		self.lbl23.setText("Good luck!")
		self.lbl23.move(300,50)
		self.lbl23.setStyleSheet('QLabel {color:blue;}')
		self.lbl21.setText("Press here and start typing--->")
		self.lbl21.move(130, 570)
		self.lbl21.resize(280,30)
		self.lbl21.setStyleSheet('QLabel {background:white;font-size:20px;}')
		self.lbl10.move(self.carplace,50)
		self.lbl6.move(self.speedplace, 70)
	def goDownReal(self):
		self.le.setText(self.le.text()[:-1])
		if self.le.text()=="":
			self.le.setStyleSheet('QLineEdit {background: white; font-size:30px;;}')
		if self.le.text()==self.length[self.probel]:
			self.le.setStyleSheet('QLineEdit {background: white; font-size:30px;;}')
	def timerEvent(self, e):
		self.time = self.time+1
		if self.time==240:
			self.doAction()
		self.wpm=int((self.enteredletters/5)//(self.time/60))
		if self.wpm==0 and self.probel!=0:
			self.doAction()
		self.lbl2.setText(str(self.wpm)+" wpm")
	def onActivated1(self, text):
		if text=="show full text":
			self.lbl1.move(200, 200)
			self.lbl1.resize(800, 300)
		else:
			self.lbl1.resize(300,20)
			self.lbl1.move(420, 450)
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
