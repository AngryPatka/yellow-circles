import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.circles = []

        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.generate_circle)

    def generate_circle(self):
        size_x, size_y = self.width(), self.height()
        x, y = randint(0, size_x), randint(0, size_y)
        r = min(min(randint(1, x), randint(1, size_x - x)), min(randint(1, y), randint(1, size_y - y)))
        self.circles.append((x, y, r))

        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor('yellow'))
        for x, y, r in self.circles:
            qp.drawEllipse(x - r, y - r, 2 * r, 2 * r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
