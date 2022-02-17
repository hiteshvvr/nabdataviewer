from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
import pyqtgraph as pg
from mainwindow import MainWindow



class MyTabWidget(QWidget):
    def __init__(self, parent,data) -> None:
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        pg.setConfigOption('background', 'w')
        self.data = data

        self.tabs = QTabWidget()
        self.tab1 = MainWindow()

        self.tabs.addTab(self.tab1, "Main Window")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

