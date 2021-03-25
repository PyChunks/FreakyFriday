from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QListWidget, QGridLayout, QLineEdit, QComboBox

from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from datetime import datetime
from PyQt5.QtCore import QDateTime, Qt, QTimer
from datetime import datetime, timedelta

import sys
import csv


class SaveScreen(QWidget):
    def __init__(self,activity):
        super(SaveScreen, self).__init__()
        self.setWindowTitle('Save')
        self.activity = activity

        self.label=QLabel('Would you like to save this Activity?')
        self.label.setAlignment(Qt.AlignCenter)
        self.yesBtn=QPushButton('Yes')
        self.noBtn=QPushButton('No, bring me home!')

        saveouterlayout = QVBoxLayout()
        labellayout = QVBoxLayout()
        btnlayout = QGridLayout()
    
        labellayout.addWidget(self.label)
        btnlayout.addWidget(self.yesBtn,0,1,1,2)
        btnlayout.addWidget(self.noBtn,0,4,1,2)
        saveouterlayout.addLayout(labellayout)
        saveouterlayout.addLayout(btnlayout)

        self.noBtn.clicked.connect(self.return_main)
        self.yesBtn.clicked.connect(self.save_activity)
        self.setLayout(saveouterlayout)

    def return_main(self):
        self.activity.return_main()
        self.activity.parent.activity_list_menu.clear()
        self.activity.parent.activity_list_menu.addItems(self.activity.parent.get_activities())
        self.close()

    def save_activity(self):
        with open('data/activity.csv', 'a', newline='') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
            datawriter.writerow([self.activity.activity_name,"start", self.activity.start_time])
            for status in self.activity.pause_list:
                datawriter.writerow([self.activity.activity_name, status[0], status[1]])
            datawriter.writerow([self.activity.activity_name,"end", self.activity.start_time])

        self.return_main()


class Activity(QWidget):
    activity_name = None
    start_time = None
    restart_time = None
    end_time = None
    duration = None
    pause_count = 0
    pause_list = []
    previous_duration = timedelta(0)



    def __init__(self,parent=None):
        super(Activity, self).__init__()
        self.setWindowTitle('QTimer example')
        self.activity_name = parent.line_menu.text()
        self.listFile=QListWidget()
        self.label=QLabel(self.activity_name)
        self.label.setAlignment(Qt.AlignCenter)
        self.startBtn=QPushButton('Start')
        self.pauseBtn=QPushButton('Pause')
        self.stopBtn=QPushButton('Stop')
        self.parent = parent

        outerlayout = QVBoxLayout()
        labellayout = QVBoxLayout()
        layout=QGridLayout()

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        labellayout.addWidget(self.label)
        layout.addWidget(self.startBtn,0,0)
        layout.addWidget(self.pauseBtn,0,1)
        layout.addWidget(self.stopBtn,2,0,1,2)
        outerlayout.addLayout(labellayout)
        outerlayout.addLayout(layout)

        self.startBtn.clicked.connect(self.startTimer)
        self.pauseBtn.clicked.connect(self.pauseTimer)
        self.stopBtn.clicked.connect(self.show_stop_screen)

        self.setLayout(outerlayout)

    def show_stop_screen(self):
        self.end_time = datetime.now()
        self.stop_screen = SaveScreen(self)
        self.stop_screen.show()
        
    def return_main(self):
        self.parent.show()
        self.close()


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
            self.pause_list.append(["unpause", datetime.now()])
            self.restart_time = datetime.now()
        print(self.start_time)
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.pauseBtn.setEnabled(True)

    def pauseTimer(self):
        self.timer.stop()
        self.pause_list.append(["pause", datetime.now()])
        self.pause_count += 1
        self.label.setText("Activity stopped\n You have worked for:\n {}\n You have taken {} breaks".format(self.time_elapsed(), self.pause_count))
        self.previous_duration = self.time_elapsed()
        self.startBtn.setEnabled(True)
        self.pauseBtn.setEnabled(False)

    def time_elapsed(self):
        current_time = datetime.now()
        self.duration = current_time - self.restart_time + self.previous_duration
        return self.duration

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.textbox = QLineEdit()
        self.textbox.setAlignment(Qt.AlignCenter)
        self.activity_list_menu = QComboBox()
        self.activity_list_menu.setEditable(True)
        self.activity_list_menu.addItems(self.get_activities())
        self.line_menu = self.activity_list_menu.lineEdit()
        self.line_menu.setAlignment(Qt.AlignCenter)
        self.button = QPushButton("Start Activity")
        self.button.clicked.connect(self.start_activity)
        layout=QGridLayout()

        layout.addWidget(self.textbox)
        layout.addWidget(self.activity_list_menu)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def start_activity(self):
       self.timer_window = Activity(self)
       self.hide()
       self.timer_window.show()

    def get_activities(self):
        with open("data/activity.csv") as f:
            reader = csv.reader(f, delimiter=',')
            activity_list = []
            a_list = set([row[0] for row in reader])
            for a in a_list:
                activity_list.append(a)
            return activity_list

if __name__ == '__main__':
    app=QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
