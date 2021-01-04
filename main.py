import sys
from random import randint

from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.circles = []

        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.generate_circle)

    def generate_circle(self):
        size_x, size_y = self.width(), self.height()
        x, y = randint(0, size_x), randint(0, size_y)
        r = min(min(randint(1, x), randint(1, size_x - x)), min(randint(1, y), randint(1, size_y - y)))
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append((x, y, r, color))

        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        for x, y, r, color in self.circles:
            qp.setBrush(QColor(*color))
            qp.drawEllipse(x - r, y - r, 2 * r, 2 * r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
