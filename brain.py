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

import command


class Brain:
    """The Brain is your primary interface to write a custom tank AI."""

    def __init__(self):
        self.memory = []

    def forget(self):
        """Forget (clear) saved command queue"""
        self.memory = []

    def face(self, direction):
        """Queue the command to change to a certain facing."""
        pass

        #if direction in Facing.values:
        #    self.memory.append(facing)
        #else:
        #    raise Exception('brain malfunction', facing)

    def forward(self):
        """Queue the command to move the tank forward.
           The direction depends on the tank's current facing."""
        self.memory.append(command.MOVE_FORWARD)

    def backward(self):
        """Queue the command to move the tank backward.
           The direction depends on the tank's current facing."""
        self.memory.append(command.MOVE_BACKWARD)

    def shoot(self):
        """Queue a shoot command.
           The direction depends on the tank's current facing."""
        self.memory.append(command.SHOOT)

    def position(self):
        """Return the (x,y) coordinate of the tank."""
        return self.tank.get_position()

    def facing(self):
        """Return the facing of the tank.
           It returns Facing.UP, Facing.DOWN, etc."""
        return self.tank.get_facing()

    def direction(self):
        """Return the facing of the tank.
           It returns (dx,dy) pointing in the direction the tank is."""
        return self.tank.get_facing_vector()

    def radar(self, x, y):
        """Return the tile information for a given coordinate.
           Returns (terrain, item). If no terrain or item, it uses None.
           See the World docs for some terrain types."""
        return self.tank.world.get_tile_enum(x, y)

    def kill(self):
        """Destroys the tank."""
        self.tank.kill()

    def think(self):
        raise NotImplementedError("You need to use a Brain implementation...")
