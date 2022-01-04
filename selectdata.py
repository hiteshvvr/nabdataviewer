import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QAction, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QFileDialog
# from testtab import MyTabWidget
from pyqtgraph import ImageView
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np

class SelectDataTab(QWidget):
    def __init__(self, parent) -> None:
        super(QWidget, self).__init__(parent)

        self.tab = QWidget()

        # Create First Tab
        # self.tab1.layout = QVBoxLayout(self)
        self.alayout = QHBoxLayout()
        self.l = QLabel()
        self.l.setText("Load Data")
        self.alayout.addWidget(self.l)

        self.button = QPushButton()
        self.button.setText("Press")
        self.button.move(50,50)
        self.button.clicked.connect(self.dialog)
 
        self.tab.setLayout(self.alayout)


    def dialog(self):
        # file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        file , check = QFileDialog.getOpenFileName(None, "nFileName()", "", "Text Files (*.root)")
        if check:
            print(file)

        
    def gettab(self):
        return(self.tab)

  

        