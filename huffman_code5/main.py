# Time: 2020/5/19-10:48
# Author: Rex

def read_file():
    pass


def encode(text):
    pass


def decode(bin_code):
    pass


def main():
    text = read_file()
    bin_code = encode(text)
    decode_text = decode(bin_code)

    print('原来的文本:', text)
    print('二进制文本:', bin_code)
    print('解码后的文本:', decode_text)
    print('是否与原文本一致？')


if __name__ == '__main__':
    main()
