from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('百度地图')
        self.setGeometry(5, 30, 1355, 730)
        self.move(50, 50)
        self.browser = QWebEngineView()
        # self.browser.load(QUrl('https://zhaosiyi.github.io/demo/?tdsourcetag=s_pcqq_aiomsg'))
        # self.browser.load(QUrl('https://www.baidu.com'))
        self.browser.load(QUrl('https://map.baidu.com'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())