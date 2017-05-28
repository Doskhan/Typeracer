from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

import sys
from datetime import datetime, timedelta

# UI base class is inherited from design.Ui_MainWindow
class Counter(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # applying background image
        self.background = QtGui.QPixmap("./assets/img/trecime.jpg")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(self.background).scale(self.size()))
        self.MainWindow.setPalette(palette)

        # custom colors for QLCDWidgets
        lcdPalette = self.dayCount.palette()
        lcdPalette.setColor(lcdPalette.WindowText, QtGui.QColor(255,0,0, 200))
        lcdPalette.setColor(lcdPalette.Background, QtGui.QColor(0, 0, 0, 0))
        lcdPalette.setColor(lcdPalette.Light, QtGui.QColor(200, 0, 0, 120))
        lcdPalette.setColor(lcdPalette.Dark, QtGui.QColor(100, 0, 0, 150))
        self.dayCount.setPalette(lcdPalette)
        lcdPalette.setColor(lcdPalette.WindowText, QtGui.QColor(255,255,255, 200))
        lcdPalette.setColor(lcdPalette.Light, QtGui.QColor(200, 0, 0, 0))
        lcdPalette.setColor(lcdPalette.Dark, QtGui.QColor(200, 0, 0, 0))
        self.timeCount.setPalette(lcdPalette)

        # init Qtimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(200)

        # config final date
        self.finalDatetime = datetime(2016, 11, 30, 14, 00)

    def resizeEvent(self, resizeEvent):
        print('resized')

    def update_timer(self):
        currentDatetime = datetime.today()
        delta = self.finalDatetime -  currentDatetime
        (days, hours, minutes) = days_hours_minutes(delta)
        self.dayCount.display(days)
        # blinking colon
        separator = ":" if delta.microseconds < 799999 else ' '
        self.timeCount.display('%02d%s%02d' % (hours, separator, minutes))

def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60

def main():
    app = QtWidgets.QApplication(sys.argv)
    counter = Counter()
    counter.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
