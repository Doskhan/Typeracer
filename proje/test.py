import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def main():
    app 	= QApplication(sys.argv)
    window	= QMainWindow()

    palette	= QPalette()
    palette.setBrush(QPalette.Background,QBrush(QPixmap("wall.png")))
    window.setPalette(palette)
    window.setWindowTitle("QMainWindow Background Image")
    window.show()

    return app.exec_()
if __name__ == '__main__':
  main()
