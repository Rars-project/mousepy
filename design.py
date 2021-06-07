import sys

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.uic import loadUiType
from finalui import Ui_ProjectUI
from gmouse import gmouse
from aimouse import aimouse

class Window(QMainWindow, Ui_ProjectUI):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.movie=QtGui.QMovie("C:\\Users\\Rohan J Billava\\Desktop\\finalyearproject\\../myjarvis/images/JxUA.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.pushButton.clicked.connect(self.firstTask)
        self.pushButton_2.clicked.connect(self.secondTask)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.thirdTask)

    def firstTask(self):
        gmouse()

    def secondTask(self):
        aimouse()

    def thirdTask(self):
        print("hello")




    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())