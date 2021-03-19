from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QListWidget, QGridLayout

from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from datetime import datetime
from PyQt5.QtCore import QDateTime, Qt, QTimer
from datetime import datetime, timedelta
import sys

class Activity(QWidget):
    start_time = None
    restart_time = None
    end_time = None
    duration = None
    pause_count = 0
    previous_duration = timedelta(0)

    def __init__(self,parent=None):
        super(Activity, self).__init__(parent)
        self.setWindowTitle('QTimer example')

        self.listFile=QListWidget()
        self.label=QLabel('Label')
        self.label.setAlignment(Qt.AlignCenter)
        self.startBtn=QPushButton('Start')
        self.pauseBtn=QPushButton('Pause')

        outerlayout = QVBoxLayout()
        labellayout = QVBoxLayout()
        layout=QGridLayout()

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        labellayout.addWidget(self.label)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.pauseBtn,1,1)
        outerlayout.addLayout(labellayout)
        outerlayout.addLayout(layout)

        self.startBtn.clicked.connect(self.startTimer)
        self.pauseBtn.clicked.connect(self.pauseTimer)

        self.setLayout(outerlayout)

    def showTime(self):
        current_time = datetime.now()
        self.duration = current_time - self.start_time
        if self.pause_count != 0:
            self.label.setText("Activity in Progress\n You've been working for:\n {}\n You have taken {} breaks".format(self.time_elapsed(), self.pause_count))
        else:
            self.label.setText("Activity in Progress\n You've been working for:\n {}\n You have taken no break yet".format(self.time_elapsed()))

    def startTimer(self):
        if (self.start_time is None):
            self.start_time = datetime.now()
            self.restart_time = self.start_time
        else:
            self.restart_time = datetime.now()
        print(self.start_time)
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.pauseBtn.setEnabled(True)

    def pauseTimer(self):
        self.timer.stop()
        self.pause_count += 1
        self.label.setText("Activity stopped\n You have worked for:\n {}\n You have taken {} breaks".format(self.time_elapsed(), self.pause_count))
        self.previous_duration = self.time_elapsed()
        self.startBtn.setEnabled(True)
        self.pauseBtn.setEnabled(False)

    def time_elapsed(self):
        current_time = datetime.now()
        # if self.previous_duration is None:
        #     self.duration = current_time - self.start_time
        # else:
        self.duration = current_time - self.restart_time + self.previous_duration
        return self.duration

class MainWindow(QWidget):
    # self.widgets = {
    # "button": [],
    # "message": [],
    # }

    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Start Activity")
        self.button.clicked.connect(self.start_activity)
        layout=QGridLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def start_activity(self, checked):
       self.timer_window = Activity()
       self.hide()
       self.timer_window.show()
        # if self.w is None:
        #     self.w = AnotherWindow()
        #     self.w.show()

        # else:
        #     self.w.close()  # Close window.
        #     self.w = None  # Discard reference.

if __name__ == '__main__':
    app=QApplication(sys.argv)
    # form=WinForm()
    # form.show()
window = MainWindow()
window.show()
sys.exit(app.exec_())
# sys.exit(app.exec_())
