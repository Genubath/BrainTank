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

MOVE_FORWARD = 1
MOVE_BACKWARD = 2

TURN_RIGHT = 3
TURN_LEFT = 4
TURN_AROUND = 5

SHOOT = 6


def command_to_string(command):
    __commands = dict()
    __commands[MOVE_FORWARD] = "move forward"
    __commands[MOVE_BACKWARD] = "move backward"
    __commands[TURN_RIGHT] = "turn right"
    __commands[TURN_LEFT] = "turn left"
    __commands[TURN_AROUND] = "turn around"
    __commands[SHOOT] = "shoot"

    return __commands[command]
