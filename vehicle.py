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

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

import state


class Tank(QWidget):
    """Draws and handles tank actions."""

    RED = "red"
    YELLOW = "yellow"
    BLUE = "blue"

    def __init__(self, world, name, color, brain):
        QWidget.__init__(self)

        self.world = world
        self.name = name
        self.color = color
        self.brain = brain

        self.facing = state.FACING_RIGHT
        self._images = dict()
        self.state = state.TANK_IDLE

        # speed is per second
        self.speed = 100
        self.reduced_speed = self.speed *0.5

    @property
    def pixmap(self):
        if self.facing not in self._images:
            pix = QPixmap("tank/%s_%s.png" % (self.color, state.facing_to_string(self.facing)))
            self._images[self.facing] = pix

        return self._images[self.facing]

    def get_next_action(self):
        return self.brain.think()
