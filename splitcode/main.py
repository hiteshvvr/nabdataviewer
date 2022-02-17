import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory
from mainframe import MyTabWidget
from mdata import MData


class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.title = "nab 60 Hz DaTa Viewer"
        self.setWindowTitle(self.title)
        data = MData()
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.tab_widget = MyTabWidget(self, data)
        self.setCentralWidget(self.tab_widget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
