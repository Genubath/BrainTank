import inspect, os

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QMainWindow, QWidget

from world import *


class BrainTankWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("BrainTank... BOOM!")
        self.setFixedSize(1024, 768)
        self.setCentralWidget(World())

        self.media_player = QMediaPlayer()
        self.media_player.stateChanged.connect(self.media_player_state_changed)
        self.play_soundtrack()

    def media_player_state_changed(self, state):
        if state == QMediaPlayer.StoppedState:
            self.play_soundtrack()

    def play_soundtrack(self):
        project_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        url = QUrl.fromLocalFile("%s/Sounds/xmasmyth.mp3" % project_dir)
        mp3 = QMediaContent(url)

        self.media_player.setMedia(mp3)
        self.media_player.setVolume(20)
        self.media_player.play()
