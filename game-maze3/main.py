import time

from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QPainter, QPen, QPalette, QResizeEvent
from PyQt5.QtWidgets import QWidget, QMessageBox
from maze_generator import generate_maze, CellType
from utils import random_maze_size


class QMaze(QWidget):
    def __init__(self, size: int):
        super(QMaze, self).__init__()

        self.MAZE, self.ENTRANCE, self.EXIT = generate_maze(size, size)
        self.ENTRANCE[0], self.ENTRANCE[1] = self.ENTRANCE[1], self.ENTRANCE[0]
        self.EXIT[0], self.EXIT[1] = self.EXIT[1], self.EXIT[0]
        print("start:{},end:{}".format(self.ENTRANCE, self.EXIT))
        self.size = size
        self.animation = None
        self.playerNode = None
        self.paintStep = 0
        self.paintOffset = 0
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.tr("Maze"))

    def draw_set(self, color=Qt.blue):
        """ PyQt绘画基本套装

        """
        pen = QPen()
        pen.setJoinStyle(Qt.RoundJoin)
        pen.setCapStyle(Qt.RoundCap)
        painter = QPainter(self)
        painter.translate(self.paintOffset)
        painter.setBackgroundMode(Qt.TransparentMode)
        painter.setRenderHint(QPainter.Antialiasing)
        pen.setWidth(0.5 * self.paintStep)
        pen.setColor(color)
        painter.setPen(pen)
        return pen, painter

    def is_path_coor(self, coordinate: list):
        x, y = coordinate
        return 0 <= x < self.size and \
               0 <= y < self.size and \
               self.MAZE[x][y] == CellType.ROAD

    def is_path(self, x, y):
        return 0 <= x < self.size and \
               0 <= y < self.size and \
               self.MAZE[x][y] == CellType.ROAD

    def drawLineCoor(self, coor1, coor2, color=Qt.yellow):
        pen, painter = self.draw_set()
        pen.setColor(color)
        painter.setPen(pen)
        x, y = coor1
        xq, yq = coor2
        self.drawLine(y, x, yq, xq, painter)

    def drawLine(self, y, x, yq, xq, painter):
        """ 重写了一个画线函数，注意像素相对位置

        """
        painter.drawLine(y * self.paintStep, x * self.paintStep,
                         yq * self.paintStep, xq * self.paintStep)

    def is_win(self, coordinate):
        return coordinate == self.EXIT

    def available_neighbors(self, coordinate, visited):
        x, y = coordinate
        neighbor_coordinates = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
        result = []
        for n in neighbor_coordinates:
            if self.is_path_coor(n) and n not in visited:
                result.append(n)
        return result

    def back_track(self):
        stack = []
        visited = []

        def _backward(now):
            # 回溯法解决迷宫问题
            stack.append(now)  # 放入栈中
            visited.append(now)  # 访问该节点
            if self.is_win(now):  # 判断是否胜利
                print("win")
                return True
            # 找到当前点所有能够到达的点
            neighbors = self.available_neighbors(now, visited)

            if neighbors:
                for n in neighbors:
                    if n not in visited:
                        #  绿色表示去程
                        # time.sleep(1)

                        self.drawLineCoor(n, now, color=Qt.green)
                        if not _backward(n):
                            last_top = stack.pop()
                            #  黄色表示折返
                            self.drawLineCoor(last_top, stack[-1], color=Qt.yellow)
                            visited.remove(last_top)
                        else:
                            return True

                return False

        _backward(self.ENTRANCE)

    def dfs(self):

        # 绘制所有节点

        visited = list()
        pen, painter = self.draw_set(color=self.palette().color(QPalette.Highlight))

        def dfs_paint(coordinate):
            nonlocal pen, painter, visited

            if self.is_win(coordinate):
                print("win")
                return True
            pen.setColor(self.palette().color(QPalette.Highlight))
            painter.setPen(pen)

            x, y = coordinate
            if self.is_path(x, y):
                visited.append(coordinate)
                neighbor_coordinates = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
                for nc in neighbor_coordinates:
                    xq, yq = nc
                    if self.is_path(xq, yq) and nc not in visited:
                        self.drawLine(y, x, yq, xq, painter)

                        return dfs_paint(nc)

                        # pen.setColor(Qt.red)
                        # painter.setPen(pen)
                        # self.drawLine(y, x, yq, xq, painter)

        dfs_paint(self.ENTRANCE)

    # 重写父类QWidgets方法paintEvent 否则不能使用样式表定义外观
    def paintEvent(self, paintEvent):
        pen, painter = self.draw_set(color=Qt.darkBlue)
        # 绘制所有节点

        visited = list()

        def dfs_paint(coordinate):
            nonlocal painter, visited
            x, y = coordinate
            if self.is_path(x, y):
                if coordinate in visited:
                    return

                visited.append(coordinate)
                neighbor_coordinates = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
                for nc in neighbor_coordinates:
                    xq, yq = nc
                    if self.is_path(xq, yq) and nc not in visited:
                        self.drawLine(y, x, yq, xq, painter)
                        dfs_paint(nc)

        dfs_paint(self.ENTRANCE)

        def draw_point(point: list, _color=Qt.green, width_scale=0.75):
            nonlocal pen, painter, paintEvent
            x, y = point
            pen.setColor(_color)
            pen.setWidth(self.paintStep * width_scale)
            painter.setPen(pen)
            painter.drawPoint(y * self.paintStep, x * self.paintStep)

        draw_point(self.ENTRANCE)
        draw_point(self.EXIT, _color=Qt.red)
        # self.playerNode = self.ENTRANCE
        # draw_point(self.playerNode, _color=self.palette().color(QPalette.Highlight),
        #            width_scale=0.9)
        del painter, pen

        self.back_track()

    def resizeEvent(self, resizeEvent: QResizeEvent):
        self.paintStep = min(self.width() / self.size, self.height() / self.size)

        self.paintOffset = QPoint((self.paintStep + (self.width() - self.paintStep * self.size)) / 2,
                                  (self.paintStep + (self.height() - self.paintStep * self.size)) / 2)

    def sizeHint(self) -> QSize:
        paintStepHint = 200
        return QSize(self.size * paintStepHint, self.size * paintStepHint)


class DfsQMaze(QMaze):
    def __init__(self, size):
        super(DfsQMaze, self).__init__(size)
        # self.dfs()


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    sys.setrecursionlimit(4000)
    application = QApplication(sys.argv)
    solver = DfsQMaze(random_maze_size())
    sys.exit(application.exec_())
