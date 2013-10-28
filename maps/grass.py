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

import maps
from tiles import *


class GrassMap(maps.AbstractMap):
    """
    Implementation of an actual usable game map
    """
    def __init__(self, width, height):
        maps.AbstractMap.__init__(self, width, height)
        for y in range(self.height):
            self._tiles.append([])
            for x in range(self.width):
                self._tiles[y].append(GrassTile())

        # set starting areas
        self._starting_areas.append((0, 0))
        self._starting_areas.append((self.width-1, 0))
        self._starting_areas.append((0, self.height-1))
        self._starting_areas.append((self.width-1, self.height-1))
