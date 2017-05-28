import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Typeracer(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setAcceptDrops(True)
		self.initUI()

	def initUI(self):
		palette = QPalette()
		palette.setBrush(QPalette.Background, QBrush(QPixmap("asd.jpg")))
		self.setPalette(palette)
		self.wrongs = 0
		self.timerstop = 1
		self.corr = 0
		pixmapCar = QPixmap("car.png").scaled(50, 70)
		self.length = []
		file = open('text.txt', 'r')
		for line in file:
			a = line.split()
			for i in a:
				self.length.append(i)

		print(self.length)

		self.step = (700-50) // len(self.length)
		self.laststep = (700-50) % len(self.length)

		self.lblCarBack = QLabel(self)
		self.lblCarBack.resize(700, 60)
		self.lblCarBack.move(250, 50)
		self.lblCarRoad = QLabel(self)
		self.lblCarRoad.resize(700, 8)
		self.lblCarRoad.move(250, 110)

		self.carplace = 250
		self.speedplace = 210

		self.lblCar = QLabel(self)
		self.lblCar.resize(50, 60)
		self.lblCar.move(self.carplace, 50)
		self.lblCar.setPixmap(pixmapCar)

		self.currenttext = ''
		self.numwrongs = 0
		for i in range(len(self.length)):
			self.currenttext += self.length[i]
			self.currenttext += " "

		self.lblUname = QLabel("You", self)
		self.lblUname.resize(40, 20)
		self.lblUname.move(self.speedplace+90, 50)

		self.lblUser = QLabel("Doskhan", self)
		self.lblUser.move(50, 10)
		self.lblUser.resize(100, 30)
		self.lblUser.setStyleSheet('QLabel {font-size:25px;color:black}')

		self.lblave = QLabel("Average: 000 wpm", self)
		self.lblave.move(10, 283)
		self.lblave.resize(220, 30)
		self.lblave.setStyleSheet('QLabel {color:black;font-size:25px;}')

		self.lblWrongs = QLabel("Wrongs:    000", self)
		self.lblWrongs.move(10, 329)
		self.lblWrongs.resize(170, 30)
		self.lblWrongs.setStyleSheet('QLabel {color:black;font-size:25px;}')

		self.lblwpm = QLabel("000 wpm", self)
		self.lblwpm.resize(140, 30)
		self.lblwpm.setStyleSheet('QLabel {color:black;font-size:25px;}')
		self.lblwpm.move(1050, 80)

		self.lblBwpm = QLabel("Best      : 000 wpm", self)
		self.lblBwpm.move(10, 410)
		self.lblBwpm.resize(200, 30)
		self.lblBwpm.setStyleSheet('QLabel {color:black;font-size:25px;}')

		self.lblTextArea = QLabel(self.currenttext, self)
		self.lblTextArea.setWordWrap(True)
		self.lblTextArea.setStyleSheet('QLabel {color:black;font-size:25px;;}')
		self.lblTextArea.move(230, 200)
		self.lblTextArea.resize(800, 200)


		self.lblFwmp = QLabel("Speed   : 000 wpm", self)
		self.lblFwmp.move(10, 362)
		self.lblFwmp.resize(220, 30)
		self.lblFwmp.setStyleSheet('QLabel {color:black;font-size:25px;}')

		self.le = QLineEdit('', self)
		self.le.move(400, 580)
		self.le.resize(400, 60)
		self.le.setPlaceholderText("Type Here")
		self.le.setStyleSheet('QLineEdit {background: white; font-size:20px;}')
		self.le.textChanged[str].connect(self.onChanged)

		self.average = 0
		self.attempts = 0
		self.bob = 0

		self.btnRestart = QPushButton('Restart', self)
		self.btnRestart.move(500, 650)
		self.btnRestart.resize(200, 50)
		self.btnRestart.setStyleSheet('QPushButton {background:white;font-family:bold; font-size:20px;}')
		self.btnRestart.clicked.connect(self.Restart)

		self.timer = QBasicTimer()
		self.time = 0
		self.timerstart = 0
		self.enteredletters = 0
		self.thebest = 0

		self.lblCheck = QLabel(self)
		self.lblCheck.move(400, 510)
		self.lblCheck.resize(400, 60)
		self.lblCheck.setStyleSheet('QLabel {background: white; font-size:20px; color:White;}')

		self.setGeometry(0, 0, 1500, 800)
		self.setWindowTitle('Type Racer')
		self.show()

	def paintEvent(self, e):

		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):

		pen = QPen(Qt.black, 2, Qt.SolidLine)
		pen.setStyle(Qt.DashDotDotLine)
		qp.setPen(pen)
		qp.drawLine(250, 110, 1000, 110)

	def onChanged(self, text):
		self.lblCheck.setText(text)
		if text!=" " and self.timerstop == 1 and self.timerstart == 0:
			self.timerstart = 1
			self.timerstop = 0
			self.timer.start(1000, self)
		if self.corr != len(self.length):
			self.currentword = self.length[self.corr]+" "
			right = 0
			for i in range(len(text)):
				if text[i] != self.currentword[i] and text != "":
					self.numwrongs += 1
					self.lblCheck.setStyleSheet('QLabel {background:red; color:black; font-size:20px}')
					print(self.currentword)
					break
				elif text != "":
					self.lblCheck.setStyleSheet('QLabel {background:white; color:black; font-size:20px}')
					right += 1
					if right == len(self.currentword):
						if self.corr == len(self.length):
							self.carplace = self.carplace + self.step + self.laststep
							self.speedplace = self.carplace-40
						else:
							self.carplace += self.step
							self.speedplace = self.carplace-40
						if self.corr != len(self.length):
							self.corr += 1
						self.lblCar.move(self.carplace, 50)
						self.lblUname.move(self.speedplace + 90, 50)
						self.moveSound = "move.wav"
						QSound.play(self.moveSound)
						self.enteredletters += len(self.currentword)
						self.lblCheck.setText("")
						self.le.setText("")
		if self.corr == len(self.length):
			self.lblCheck.setText("Press Restart button to Try again!")
			self.lblCheck.setStyleSheet('QLabel {background:white;font-size:25px;}')
		if text == "":
			self.lblCheck.setStyleSheet('QLabel {background:white;}')

	def Restart(self):
		self.timer.stop()
		self.timerstop = 1
		self.timerstart = 0
		self.time = 0
		self.wrongs = 0
		self.enteredletters = 0
		self.corr = 0
		self.carplace = 250
		self.speedplace = 210
		self.lblwpm.setText("000 wpm")

		self.lblWrongs.setText("Wrongs:  000")
		self.lblFwmp.setText("Speed:    000 wpm")

		self.le.setText('')
		self.le.setPlaceholderText("Type Here")
		self.le.setStyleSheet('QLineEdit {background: white; font-size:20px;}')


		self.lblCar.move(self.carplace, 50)
		self.lblUname.move(self.speedplace, 70)

	def timerEvent(self, e):
		self.time = self.time+1
		if self.time == 240:
			self.Restart()
		self.wpm = int((self.enteredletters/5)//(self.time/60))
		if self.wpm == 0 and self.corr != 0:
			self.Restart()
		self.lblwpm.setText(str(self.wpm) + " wpm")
		if self.corr == len(self.length) - 1:
			self.timer.stop()
			if self.attempts == 0:
				self.bob = self.wpm
				self.lblBwpm.setText("Best: "+str(self.bob)+" wpm")
			else:
				if self.wpm > self.bob:
					self.bob = self.wpm
					self.lblBwpm.setText("Best: "+str(self.bob)+" wpm")
			self.attempts += 1
			self.average += self.wpm
			avv = self.average//self.attempts
			self.lblWrongs.setText("Wrongs: "+str(self.numwrongs))
			self.lblFwmp.setText("Speed: "+str(self.wpm)+" wpm")
			self.lblave.setText("Average: "+str(avv)+" wpm")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Typeracer()
	sys.exit(app.exec_())
