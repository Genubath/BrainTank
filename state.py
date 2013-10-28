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

TANK_IDLE     = 1
TANK_TURNING  = 2
TANK_SHOOTING = 3
TANK_MOVING   = 4
TANK_DEAD     = 5

FACING_UP     = 6
FACING_RIGHT  = 7
FACING_DOWN   = 8
FACING_LEFT   = 9


def facing_to_string(facing):
    if facing == FACING_UP:
        return "up"
    elif facing == FACING_DOWN:
        return "down"
    elif facing == FACING_LEFT:
        return "left"
    else:
        return "right"
