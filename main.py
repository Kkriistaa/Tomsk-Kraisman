import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class QMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setFixedSize(800, 600)
        self.initUI()

    def initUI(self):
        self.pushButton.setChecked(False)
        self.count = randint(1, 10)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.pushButton.hide()
        self.do_paint = True
        self.update()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(self.count):
            di = randint(10, 300)
            qp.drawEllipse(randint(di, 800 - di), randint(di, 600 - di), di, di)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QMainWindow()
    ex.show()
    sys.exit(app.exec())