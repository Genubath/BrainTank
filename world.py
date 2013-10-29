#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
# Python AI Battle
#
# Copyright 2011 Matthew Thompson
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

from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

from brains.wander import WanderBrain
import maps
from vehicle import Tank


class World(QWidget):
    game_over = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.map = maps.GrassMap(self, 10, 10)

        red_tank = Tank(self, "David Vestal", Tank.RED, WanderBrain())
        self.add_tank(red_tank)

        yellow_tank = Tank(self, "David Tennant", Tank.YELLOW, WanderBrain())
        self.add_tank(yellow_tank)

        blue_tank = Tank(self, "Matt Smith", Tank.BLUE, WanderBrain())
        self.add_tank(blue_tank)

        # timer to trigger the map updates
        self.event_timer = QTimer(self)
        self.event_timer.timeout.connect(self.map.update)
        self.event_timer.start(100)  # will execute every 100 milliseconds (10 times per second)

    def paintEvent(self, paint_event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.map.render_map(painter)

    def add_tank(self, tank):
        self.map.add_tank(tank)


