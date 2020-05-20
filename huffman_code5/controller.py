# -*- coding: UTF-8 -*-
"""
@Project -> File   ：task6-huffman-tree -> main
@IDE    ：PyCharm
@Author ：QiangZiBro
@Date   ：2020/5/19 2:27 下午
@Desc   ： 使用哈夫曼编码进行文件压缩与解压缩
        读文件 -->  统计字母频数 --> 构建哈弗曼树
        --> 编码 --> 解码
"""
from collections import defaultdict

FILENAME = "./alice.txt"


class TreeNode(object):
    """ 一个树节点，可以用于构建哈弗曼树
    """

    def __init__(self, frequency, character=''):
        self.left = None
        self.right = None
        self.frequency = frequency
        self.character = character

    def setLeftChild(self, left):
        self.left = left

    def setRightChild(self, right):
        self.right = right

    def isSingleNode(self):
        return self.left is None and self.right is None

    @classmethod
    def createNode(cls, item):
        """根据一个输入元祖初始一个节点
        :param item:
        :return:
        """
        return TreeNode(item[1], item[0])


def read_from_file(filename):
    """ 读文件
    :param filename:  文件名
    :return:  文件流
    """
    return open(filename,'r',encoding = 'utf-8')


def character_count(file_stream):
    """ 统计词频
        【建议】字典可以使用python的`defaultdict`对象，
        使用方法1：
    :param file_stream:
    :return: word_frequency [(character:frequency) ...] 字母频率
    """
    # 1.统计词频
    word_frequency = defaultdict(lambda: 0)
    while True:
        c = file_stream.read(1)
        if not c:
            break
        word_frequency[c] += 1
    # 2.对字典按值排序
    word_frequency = sorted(word_frequency.items(),
                            key=lambda x: x[1],  # 按第二个元素排序
                            reverse=False)
    return word_frequency


def create_huffman_tree(word_frequency):
    """ 通过字母频率创建哈弗曼树
    :param word_frequency:list
    :return: root：哈弗曼根节点
    """

    def grow(left_child, right_child):
        """ 输入两个子节点，生长成一个根节点，注意根节点是两个子节点词频之和
        """
        root = TreeNode(left_child.frequency + right_child.frequency)
        root.setLeftChild(left_child)
        root.setRightChild(right_child)
        return root

    if len(word_frequency) == 0:
        raise Exception("File is empty")

    if len(word_frequency) == 1:
        return TreeNode(frequency=word_frequency[0][1], character=word_frequency[0][0])

    # len(word_frequency) > 1
    left, right = word_frequency.pop(0), word_frequency.pop(0)
    left_child, right_child = TreeNode.createNode(left), TreeNode.createNode(right)
    root = grow(left_child, right_child)
    while word_frequency:
        left = word_frequency.pop(0)
        left_child = TreeNode.createNode(left)
        root = grow(left_child, root)
    return root


def character_to_bin(node):
    """ 使用哈弗曼树，构建一个由字符到二进制的字典
    :param node:
    :return:
    """

    def dfs(node, code, result):
        left = node.left
        right = node.right
        if left.isSingleNode() and right.isSingleNode():
            result[left.character] = code + '0'
            result[right.character] = code + '1'
            return result
        else:
            result[left.character] = code + '0'
            return dfs(node.right, code + '1', result)

    result = dict()

    if node.isSingleNode():
        result[node.character] = '1'
        return result
    else:
        return dfs(node, '1', result)


def encoding(character_bin_dict, file_stream, to_file="./output.bin"):
    """
    :param character_bin_dict:  字符--二进制的对应
    :param file_stream: 文件流
    :param to_file:
    :return:
    """
    result = ""
    file_stream.seek(0)
    while True:
        c = file_stream.read(1)
        if not c:
            break
        result += character_bin_dict[c]
    with open(to_file, 'w') as f:
        f.write(result)
    return result


def decoding(encoding_stream, character_bin_dict, to_file="./decoding_result.txt"):
    """ 解码
    :param encoding_stream:  二进制文件流
    :param character_bin_dict:  字符--词频的对应
    :param to_file: 输出文件结果
    :return:
    """
    bin_character_dict = {value: key for key, value in character_bin_dict.items()}
    result = ""  # 保存解码结果
    character_bin = ""  # 存在的字符的二进制
    keys = bin_character_dict.keys()
    while True:
        c = encoding_stream.read(1)
        if not c:
            break
        character_bin += c
        if character_bin in keys:
            result += bin_character_dict[character_bin]
            character_bin = ""
    with open(to_file, 'w') as f:
        f.write(result)
    return result


def getEncoding(filename, encoding_filename='output.bin'):
    file_stream = read_from_file(filename)
    word_frequency = character_count(file_stream)
    root = create_huffman_tree(word_frequency)
    bin_dict = character_to_bin(root)
    return encoding(bin_dict, file_stream, encoding_filename)


def getDecoding(filename,encoding_filename='output.bin',decoding_filename='decoding_result.txt'):

    file_stream = read_from_file(filename)
    word_frequency = character_count(file_stream)
    root = create_huffman_tree(word_frequency)
    bin_dict = character_to_bin(root)
    encoding_stream = read_from_file(encoding_filename)
    return decoding(encoding_stream, bin_dict, decoding_filename)


def main(filename, encoding_filename='output.bin', decoding_filename='decoding_result.txt'):
    print("打开文件：{}".format(filename))
    file_stream = read_from_file(filename)
    word_frequency = character_count(file_stream)
    root = create_huffman_tree(word_frequency)
    bin_dict = character_to_bin(root)

    print("编码成功，输出到{}".format(encoding_filename))
    encoding(bin_dict, file_stream, encoding_filename)

    print("解码结果到{}".format(decoding_filename))
    encoding_stream = read_from_file(encoding_filename)
    decoding(encoding_stream, bin_dict, decoding_filename)

    file_stream.close()


if __name__ == "__main__":
    main('test.txt', 'output.bin', 'decoding_result.txt')