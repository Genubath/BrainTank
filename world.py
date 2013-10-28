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

import uuid

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget

from vehicle import Tank


class World(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.tanks = []
        self.map = GrassMap(10, 10)

        red_tank = Tank(self, Tank.RED)
        self.add_tank(red_tank)

        yellow_tank = Tank(self, Tank.YELLOW)
        self.add_tank(yellow_tank)

        blue_tank = Tank(self, Tank.BLUE)
        self.add_tank(blue_tank)

    def paintEvent(self, paint_event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.map.render_map(painter)

    def add_tank(self, tank):
        self.tanks.append(tank)
        self.map.add_tank(tank)


