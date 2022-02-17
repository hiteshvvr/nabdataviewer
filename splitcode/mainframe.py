from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
import pyqtgraph as pg
from mainwindow import MainWindow
from mdata import MData



class MainFrame(QWidget):
    def __init__(self, parent) -> None:
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        pg.setConfigOption('background', 'w')

        self.tabs = QTabWidget()
        self.data = MData()
        self.tab1 = MainWindow(self.data)

        self.tabs.addTab(self.tab1, "Main Window")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

