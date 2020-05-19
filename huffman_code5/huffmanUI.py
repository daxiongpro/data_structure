# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'huffmanUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 130, 464, 52))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_open = QtWidgets.QPushButton(self.widget)
        self.pushButton_open.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout.addWidget(self.pushButton_open)
        self.pushButton_encode = QtWidgets.QPushButton(self.widget)
        self.pushButton_encode.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_encode.setObjectName("pushButton_encode")
        self.horizontalLayout.addWidget(self.pushButton_encode)
        self.pushButton_decode = QtWidgets.QPushButton(self.widget)
        self.pushButton_decode.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_decode.setObjectName("pushButton_decode")
        self.horizontalLayout.addWidget(self.pushButton_decode)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(90, 240, 501, 391))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget1)
        self.groupBox.setObjectName("groupBox")
        self.textEdit_text = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_text.setGeometry(QtCore.QRect(10, 30, 471, 81))
        self.textEdit_text.setObjectName("textEdit_text")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_encode = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_encode.setGeometry(QtCore.QRect(10, 30, 471, 81))
        self.textEdit_encode.setObjectName("textEdit_encode")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_decode = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_decode.setGeometry(QtCore.QRect(10, 30, 471, 81))
        self.textEdit_decode.setObjectName("textEdit_decode")
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_open.setText(_translate("MainWindow", "open"))
        self.pushButton_encode.setText(_translate("MainWindow", "encode"))
        self.pushButton_decode.setText(_translate("MainWindow", "decode"))
        self.groupBox.setTitle(_translate("MainWindow", "导入的文本"))
        self.groupBox_2.setTitle(_translate("MainWindow", "encode码"))
        self.groupBox_3.setTitle(_translate("MainWindow", "decode码"))
