import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QAction, QTabWidget, QVBoxLayout, QLabel
# from testtab import MyTabWidget
from pyqtgraph import ImageView
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np

from selectdata import SelectDataTab

class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.title = "Main Window"
        self.setWindowTitle(self.title)
        
        # self.tab_widget = MyTabWidget(self)
        # self.setCentralWidget(self.tab_widget)

        self.show()


class MyTabWidget(QWidget):
    def __init__(self, parent) -> None:
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        pg.setConfigOption('background', 'w')

        # Initialize tab screen 
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.loaddata = SelectDataTab()
        self.loaddatatab = self.loaddata.gettab()


        self.height = 30
        self.width = 100

        # Add tabs
        self.tabs.addTab(self.tab1, "All Data")
        self.tabs.addTab(self.tab2, "Monitor 1")
        self.tabs.addTab(self.tab3, "Monitor 2")

        # Create First Tab
        # self.tab1.layout = QVBoxLayout(self)
        self.alayout = QVBoxLayout()
        self.l = QLabel()
        self.l.setText("This is First Tab")
        # self.tab1.layout.addWidget(self.l)
        self.alayout.addWidget(self.l)
        # self.tab1.setLayout(self.tab1.layout)
        self.setallVolt = QPushButton('SetAllVolt')
        self.setallVolt.setMaximumHeight(self.height)
        self.setallVolt.setMaximumWidth(self.width)


        # self.gwin = pg.GraphicsWindow()
        # self.rplt = self.gwin.addPlot()
        
        self.pen1 = pg.mkPen('r', width=2)
        self.pen2 = pg.mkPen(color=(255, 15, 15),width=2)
        # self.pen3 = pg.mkPen(color=(000, 155, 115), style=QtCore.Qt.DotLine)
        # self.curve = self.rplt.plot(pen=self.pen3)
        # self.curve2 = self.rplt.plot(pen=self.pen2)
        # self.rplt.showGrid(x=True, y=True)
        # self.data = np.arange(100)
        # self.avg_data = []
        # self.count = 0
        # self.curve.setData(self.data)

        self.pw = pg.PlotWidget(name="testplot")
        self.p1 = self.pw.plot()
        self.p1.setPen(color = (200,20,10), width = 5)

        self.pw.setLabel('left', 'Value', units='V')
        self.pw.setLabel('bottom', 'Time', units='s')
        self.hb = QHBoxLayout()
	
        self.b3 = QPushButton("Button3")
        self.b4 = QPushButton("Button4")
        self.hbox.addWidget(b3)
        self.hbox.addStretch()
        self.hbox.addWidget(b4)

        # self.pw.setXRange(0, 10)
        # self.pw.setYRange(0, 1e-3)

        self.x = np.arange(10)
        self.y = np.sqrt(self.x)

        self.p1.setData(x=self.x, y = self.y)
        self.pw.showGrid(x=True, y=True)






        self.alayout.addWidget(self.setallVolt)
        # self.alayout.addWidget(self.gwin)
        self.alayout.addWidget(self.pw)



        self.tab1.setLayout(self.alayout)
        self.tab1.setLayout(self.alayout)

        #Add tabs to Widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    tab_widget = MyTabWidget(ex)
    ex.setCentralWidget(tab_widget)
    sys.exit(app.exec_())

    

