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

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPixmap


class Tile:
    # possible tile types
    DIRT = 'dirt'
    GRASS = 'grass'
    WATER = 'water'

    def __init__(self):
        self.type = None
        self.pixmap = None

    @staticmethod
    def bounding_box():
        return QRectF(0, 55, 101, 77)


class DirtTile(Tile):
    def __init__(self):
        Tile.__init__(self)
        self.type = Tile.DIRT
        self.pixmap = QPixmap("PlanetCute/Dirt_Block.png")


class GrassTile(Tile):
    def __init__(self):
        Tile.__init__(self)
        self.type = Tile.GRASS
        self.pixmap = QPixmap("PlanetCute/Grass_Block.png")