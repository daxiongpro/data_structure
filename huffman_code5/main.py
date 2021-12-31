# Time: 2020/5/19-10:48
# Author: Rex
import sys

from PyQt5.QtWidgets import QApplication

from huffman_code5.view import MyHuffmanWindow


def read_file():
    pass


def encode(text):
    pass


def decode(bin_code):
    pass


def main2():
    text = read_file()
    bin_code = encode(text)
    decode_text = decode(bin_code)

    print('原来的文本:', text)
    print('二进制文本:', bin_code)
    print('解码后的文本:', decode_text)
    print('是否与原文本一致？')


def main():
    app = QApplication(sys.argv)
    huffman = MyHuffmanWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
