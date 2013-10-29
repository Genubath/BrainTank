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

from PyQt5.QtGui import QPainter

from vehicle import *


class AbstractMap:
    def __init__(self, world, width, height):
        self.world = world
        self.width = width
        self.height = height
        self._tiles = []
        self._destructibles = dict()
        self._tanks = dict()
        self._projectiles = dict()
        self._starting_areas = []

    def add_tank(self, tank: Tank):
        _start_tile = self._starting_areas.pop(0)
        _id = uuid.uuid4()
        self._tanks[_id] = (_start_tile, tank)

    def add_projectile(self, bullet: Bullet, tile: tuple):
        _id = uuid.uuid4()
        self._projectiles[_id] = (tile, bullet)

    @staticmethod
    def tile_at(point: tuple):
        _x, _y = point
        return _x*101, _y*77

    def render_map(self, painter: QPainter):
        self._render_background(painter)
        self._render_destructibles(painter)
        self._render_tanks(painter)
        self._render_projectiles(painter)

    def _render_background(self, painter: QPainter):
        for y in range(self.height):
            for x in range(self.width):
                tile = self._tiles[y][x]
                box = tile.bounding_box()
                painter.drawPixmap(101*x, 77*y, tile.pixmap, box.x(), box.y(), box.width(), box.height())

    def _render_destructibles(self, painter: QPainter):
        pass

    def _render_projectiles(self, painter: QPainter):
        for _id, bullet_info in self._projectiles.items():
            _tile, bullet = bullet_info
            x, y = AbstractMap.tile_at(_tile)
            painter.drawPixmap(x, y, bullet.pixmap)

    def _render_tanks(self, painter: QPainter):
        for _id, tank_info in self._tanks.items():
            _tile, tank = tank_info
            x, y = AbstractMap.tile_at(_tile)
            painter.drawPixmap(x, y, tank.pixmap)
