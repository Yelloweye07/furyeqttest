from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel,QLineEdit)
from instr import * 

class SecondWin(QWidget):
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
        self.timer = QLabel('00:00:00')
        self.timer.setStyleSheet("font: bold 50px")
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
        self.right_line.addWidget(self.timer)
        self.horizontal_line.addLayout(self.left_line)
        self.horizontal_line.addLayout(self.right_line)
        self.setLayout(self.horizontal_line)
    def connects(self):
        pass
    def __init__ (self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
app = QApplication([])
sw = SecondWin()
app.exec_()