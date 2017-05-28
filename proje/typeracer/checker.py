#KEY EVENT
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Example(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Event handler')
		self.show()

	def keyPressEvent(self, e):
		QMessageBox.information(self, "KEY WAS PRESSED", str(e.key()))


if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
