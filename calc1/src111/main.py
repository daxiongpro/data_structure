import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from src111.myCalcUI import Ui_MainWindow


class MyCalculator(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyCalculator,self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()

    def connecter(self):
        self.pushButton_1.clicked.connect(self.press_1)
        self.pushButton_2.clicked.connect(self.press_2)
        self.pushButton_3.clicked.connect(self.press_3)
        self.pushButton_4.clicked.connect(self.press_4)
        self.pushButton_5.clicked.connect(self.press_5)
        self.pushButton_6.clicked.connect(self.press_6)
        self.pushButton_7.clicked.connect(self.press_7)
        self.pushButton_8.clicked.connect(self.press_8)
        self.pushButton_9.clicked.connect(self.press_9)
        self.pushButton_0.clicked.connect(self.press_0)
        self.pushButton_DEL.clicked.connect(self.press_DEL)
        self.pushButton_point.clicked.connect(self.press_point)
        self.pushButton_plus.clicked.connect(self.press_plus)
        self.pushButton_sub.clicked.connect(self.press_sub)
        self.pushButton_mul.clicked.connect(self.press_mul)
        self.pushButton_div.clicked.connect(self.press_div)
        self.pushButton_AC.clicked.connect(self.press_AC)
        self.pushButton_equal.clicked.connect(self.press_equal)

    def press_0(self):
        self.lineEdit.insert("0")

    def press_1(self):
        self.lineEdit.insert("1")

    def press_2(self):
        self.lineEdit.insert('2')

    def press_3(self):
        self.lineEdit.insert('3')

    def press_4(self):
        self.lineEdit.insert('4')

    def press_5(self):
        self.lineEdit.insert('5')

    def press_6(self):
        self.lineEdit.insert('6')

    def press_7(self):
        self.lineEdit.insert('7')

    def press_8(self):
        self.lineEdit.insert('8')

    def press_9(self):
        self.lineEdit.insert('9')

    def press_point(self):
        self.lineEdit.insert(".")

    def press_DEL(self):
        self.lineEdit.backspace()

    def press_mul(self):
        self.lineEdit.insert("*")

    def press_div(self):
        self.lineEdit.insert("/")

    def press_plus(self):
        self.lineEdit.insert("+")

    def press_sub(self):
        self.lineEdit.insert("-")

    def press_AC(self):
        self.lineEdit.setText("")

    def press_equal(self):
        text = self.lineEdit.text()
        try:
            result = eval(text)
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText("Invalid syntax, check your input!")



def main():
    app = QApplication(sys.argv)
    Calc = MyCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
