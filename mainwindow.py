from PyQt5.QtWidgets import QApplication, QMainWindow ,QWidget

from world import *

class BrainTankWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("BrainTank... BOOM!")
        self.setFixedSize(1024, 768)

        self.world = World()
        self.setCentralWidget(self.world)