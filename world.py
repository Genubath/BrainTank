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

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget

import state
import vehicle

#class Tile(QGraphicsPixmapItem):
#    def __init__(self, parent=None):
#        QGraphicsPixmapItem.__init__(self, parent)
#
#
#class DirtTile(Tile):
#    def __init__(self):
#        Tile.__init__(self)
#        self.setPixmap(QPixmap("PlanetCute/Dirt_Block.png"))
#
#
#class GrassTile(Tile):
#    def __init__(self):
#        Tile.__init__(self)
#        self.setPixmap(QPixmap("PlanetCute/Grass_Block.png"))


class World(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.tanks = []

        red_tank = vehicle.Tank(self, state.FACING_UP, "red")
        self.tanks.append(red_tank)

    def paintEvent(self, paint_event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.render_map_background(painter)
        self.render_tanks(painter)

    def render_tanks(self, painter):
        """
        @type painter: QPainter
        """
        for t in self.tanks:
            painter.drawPixmap(200, 200, t.pixmap)

    def add_tank(self, t):
        pass

    @staticmethod
    def render_map_background(painter):
        pixmap = QPixmap("PlanetCute/Grass_Block.png")
        painter.drawPixmap(0, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 0, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 77, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 154, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 231, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 308, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 385, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 462, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 539, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 616, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 693, pixmap, 0, 55, 101, 77)


class Map:
    def __init__(self):
        pass
