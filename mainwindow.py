from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QWidget

from world import *


class BrainTankWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("BrainTank... BOOM!")
        self.setFixedSize(1024, 768)
        self.setCentralWidget(World())
