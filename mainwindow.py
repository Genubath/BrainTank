# -*- coding: utf-8 -*-

###############################################################################
# Python AI Battle
#
# Copyright 2013 David Vestal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

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
