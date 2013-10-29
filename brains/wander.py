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

import random

from brains import Brain
import command


class WanderBrain(Brain):
    """
    Wander Brain

    This is a sample wandering brain. It just drives until it
    hits an obstacle then chooses a new direction. It also changes
    direction periodically.

    Variables available to brains:
        color - string, tank color
        position - tuple (x,y), current tank grid position
        facing - symbol UP, DOWN, LEFT, RIGHT, current tank facing
        direction - tuple (x,y), unit vector representing tank facing
        shots - how many shots have been fired
        tanks - list of other tanks in map
        tank_positions - [(x,y)] other tank positions
        tank_states - list of other tank states (see Tank States)

    Functions available to brains:
        memory() - returns [symbol], a read only copy of queued commands
        forget() - clear all queued brain commands
        face(symbol) - change tank facing to symbol UP, DOWN, LEFT, or RIGHT
        forward() - move tank forward one space
        backward() - move tank backward one space
        shoot() - fire tank's weapon with current facing
        radar(x,y) - get a tuple (tile, item) from the map's x,y coordinate
        kill() - self destruct tank

    Facings:
        UP, DOWN, LEFT, RIGHT,

    Brain Commands:
        FORWARD, BACKWARD, SHOOT

    Tank States:
        IDLE, MOVING, TURNING, SHOOTING, DEAD

    Tiles:
        GRASS, DIRT, PLAIN, WATER
        SAFE_TILES = (GRASS, DIRT, PLAIN) - can be driven on safely
        UNSAFE_TILES = (WATER,) - will destroy your tank if you drive into them

    Items:
        ROCK, TREE - blocking items that can be destroyed
        TANK_BLUE, TANK_RED - tanks located on a tile

    Lookup Helper Dictionaries:
        FACING_TO_VEC - takes a facing symbol and returns the (x,y) unit vector

    """

    def __init__(self):
        Brain.__init__(self)
        self._world = None
        self.rand = random.SystemRandom()

    @property
    def world(self):
        if self._world is None:
            raise AttributeError("world was not set")
        return self._world

    def set_world(self, world):
        self._world = world

    def think(self):
        """
        This brain will make a weighted random choice for each action. There is a 10% chance that it will choose
        to shoot.  If it does not shoot then it will "roll the dice" again to see what other action it will take.
        """
        choice = self.rand.randint(1, 100)
        if choice <= 10:
            return command.SHOOT

        return self.rand.randint(1, 5)
