
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel,QLineEdit)
from instr import * 
from final_win import *

class SecondWin(QWidget):
    def timer_test(self):
       global time 
       time = QTime(0, 1, 0)
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer1Event)
       self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timerLabel.setText(time.toString("hh:mm:ss"))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        global time 
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timerLabel.setText(time.toString("hh:mm:ss")[6:8])
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_final(self):
       global time 
       time = QTime(0, 1, 0)
       self.timer = QTimer()
       self.timer.timeout.connect(self.timer3Event)
       self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timerLabel.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.timerLabel.setStyleSheet("color: rgb(0,255,0); font: bold 50px")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timerLabel.setStyleSheet("color: rgb(0,255,0); font: bold 50px")
        else:
            self.timerLabel.setStyleSheet("color: rgb(0,0,0); font: bold 50px")
    def set_appear(self):
        pass
    def initUI(self):
        self.name = QLabel(txt_name)
        self.nameanswer = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.ageAnswer = QLineEdit(txt_hintage)
        self.question1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.test1hint = QLineEdit(txt_hinttest1)
        self.question2 = QLabel(txt_test2)
        self.starttest2 = QPushButton(txt_starttest2)
        self.question3 = QLabel(txt_test3)
        self.starttest3 = QPushButton(txt_starttest3)
        self.test2hint = QLineEdit(txt_hinttest2)
        self.test3hint = QLineEdit(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.timerLabel = QLabel('00:00:00')
        self.timerLabel.setStyleSheet("font: bold 50px")
        self.horizontal_line = QHBoxLayout()
        self.right_line = QVBoxLayout()
        self.left_line = QVBoxLayout()
        self.left_line.addWidget(self.name,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.nameanswer,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.age,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.ageAnswer,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.question1,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.starttest1,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.test1hint,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.question2,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.starttest2,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.question3,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.starttest3,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.test2hint,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.test3hint,alignment = Qt.AlignLeft)
        self.left_line.addWidget(self.sendresults,alignment = Qt.AlignLeft)
        self.right_line.addWidget(self.timerLabel)
        self.horizontal_line.addLayout(self.left_line)
        self.horizontal_line.addLayout(self.right_line)
        self.setLayout(self.horizontal_line)
    def connects(self):
        self.sendresults.clicked.connect(self.next_click)
        self.starttest1.clicked.connect(self.timer_test)
        self.starttest2.clicked.connect(self.timer_sits)
        self.starttest3.clicked.connect(self.timer_final)
    def __init__ (self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def next_click(self):
        self.hide()
        self.tw = WinThree()

app = QApplication([])
mw = SecondWin()
app.exec_()