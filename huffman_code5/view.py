# Time: 2020/5/19-11:05
# Author: Rex

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from huffman_code5.huffmanUI import Ui_MainWindow

from huffman_code5.controller import *


class MyCalcWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyCalcWindow, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()

    def connecter(self):
        self.pushButton_open.clicked.connect(self.press_open)
        self.pushButton_encode.clicked.connect(self.press_encode)
        self.pushButton_decode.clicked.connect(self.press_decode)

    def press_open(self):
        fileName, imgType = QFileDialog.getOpenFileName(self, "打开txt文件", "", "*.txt;;All Files(*)")
        self.file = fileName
        print(type(fileName))
        try:
            with open(fileName, mode='r', encoding='utf-8') as f:
                text_list = f.readlines()
                text = ''.join(text_list)
                self.textEdit_text.setText(text)
        except Exception as e:
            print(e)

    def press_encode(self):
        bin = getEncoding(filename=self.file)
        self.textEdit_encode.setText(bin)
    def press_decode(self):
        decodes = getDecoding(filename=self.file)
        self.textEdit_decode.setText(decodes)
