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

import uuid

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QPixmap

from vehicle import Tank

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


class AbstractMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._tiles = []
        self._tanks = []
        self._starting_areas = []

    def add_tank(self, tank: Tank):
        _start_tile = self._starting_areas.pop(0)
        _x, _y = AbstractMap.tile_at(_start_tile)
        _id = uuid.uuid4()
        self._tanks.append((_id, _x, _y, tank))

    @staticmethod
    def tile_at(point: tuple):
        _x, _y = point
        return _x*101, _y*77

    def render_map(self, painter):
        """
        @type painter: QPainter
        """
        self._render_background(painter)
        self._render_tanks(painter)
        # render deductibles
        # render tanks

    def _render_background(self, painter):
        """
        @type painter: QPainter
        """
        for y in range(self.height):
            for x in range(self.width):
                tile = self._tiles[y][x]
                box = tile.bounding_box()
                painter.drawPixmap(101*x, 77*y, tile.pixmap, box.x(), box.y(), box.width(), box.height())

    def _render_tanks(self, painter):
        for tinfo in self._tanks:
            _id, _x, _y, _tank = tinfo
            painter.drawPixmap(_x, _y, _tank.pixmap)


class GrassMap(AbstractMap):
    """
    Implementation of an actual usable game map
    """
    def __init__(self, width, height):
        AbstractMap.__init__(self, width, height)
        for y in range(self.height):
            self._tiles.append([])
            for x in range(self.width):
                self._tiles[y].append(GrassTile())

        # set starting areas
        self._starting_areas.append((0, 0))
        self._starting_areas.append((self.width-1, 0))
        self._starting_areas.append((0, self.height-1))
        self._starting_areas.append((self.width-1, self.height-1))
