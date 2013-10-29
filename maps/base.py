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

from PyQt5.Qt import pyqtSlot

import command
from maps import AbstractMap
import state


class BaseMap(AbstractMap):

    @pyqtSlot()
    def update(self):
        # for each tank check to see if it has an action
        # if it does... update it... if not ask for another action
        for _id, tank_info in self._tanks.items():
            _tile, tank = tank_info
            if tank.state is state.TANK_IDLE:
                _action = tank.get_next_action()
                _updated_info = self.move_it(_action, tank_info)
                self._tanks[_id] = _updated_info

        # for each projectile... update it...
        for boom in self._projectiles:
            pass

        self.world.update()

    def move_it(self, _action, tank_info: tuple):
        _tile, tank, = tank_info

        # move forward
        if _action == command.MOVE_FORWARD:
            return self.move_forward(tank_info)

        # move backward
        elif _action == command.MOVE_BACKWARD:
            return self.move_backward(tank_info)

        # turn left
        elif _action == command.TURN_LEFT:
            if tank.facing == state.FACING_RIGHT:
                tank.facing = state.FACING_UP
            elif tank.facing == state.FACING_DOWN:
                tank.facing = state.FACING_RIGHT
            elif tank.facing == state.FACING_LEFT:
                tank.facing = state.FACING_DOWN
            elif tank.facing == state.FACING_UP:
                tank.facing = state.FACING_LEFT

        # turn right
        elif _action == command.TURN_RIGHT:
            if tank.facing == state.FACING_RIGHT:
                tank.facing = state.FACING_DOWN
            elif tank.facing == state.FACING_DOWN:
                tank.facing = state.FACING_LEFT
            elif tank.facing == state.FACING_LEFT:
                tank.facing = state.FACING_UP
            elif tank.facing == state.FACING_UP:
                tank.facing = state.FACING_RIGHT

        # turn around
        elif _action == command.TURN_AROUND:
            if tank.facing == state.FACING_RIGHT:
                tank.facing = state.FACING_LEFT
            elif tank.facing == state.FACING_LEFT:
                tank.facing = state.FACING_RIGHT
            elif tank.facing == state.FACING_DOWN:
                tank.facing = state.FACING_UP
            elif tank.facing == state.FACING_UP:
                tank.facing = state.FACING_DOWN
            else:
                # this should never happen... restoring sanity to the world
                tank.facing = state.FACING_RIGHT
            return _tile, tank

        # shoot
        elif _action == command.SHOOT:
            pass

        # something bad happened
        else:
            print("Tank [%s] issued unknown action %s" % (tank.name, _action))
        return tank_info

    def move_forward(self, tank_info):
        _tile, tank = tank_info
        if tank.facing == state.FACING_RIGHT:
            return self.move_right(tank_info)
        elif tank.facing == state.FACING_LEFT:
            return self.move_left(tank_info)
        elif tank.facing == state.FACING_UP:
            return self.move_up(tank_info)
        elif tank.facing == state.FACING_DOWN:
            return self.move_down(tank_info)
        return tank_info

    def move_backward(self, tank_info):
        _tile, tank = tank_info
        if tank.facing == state.FACING_RIGHT:
            return self.move_left(tank_info)
        elif tank.facing == state.FACING_LEFT:
            return self.move_right(tank_info)
        elif tank.facing == state.FACING_UP:
            return self.move_down(tank_info)
        elif tank.facing == state.FACING_DOWN:
            return self.move_up(tank_info)
        return tank_info

    def move_up(self, tank_info):
        _tile, tank = tank_info
        x, y = _tile
        new_y = y-1
        if new_y >= 0:
            _tile = (x, new_y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return tank_info

    def move_down(self, tank_info):
        _tile, tank = tank_info
        x, y = _tile
        new_y = y+1
        if new_y < self.height:
            _tile = (x, new_y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return tank_info

    def move_left(self, tank_info):
        _tile, tank = tank_info
        x, y = _tile
        new_x = x-1
        if new_x >= 0:
            _tile = (new_x, y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return tank_info

    def move_right(self, tank_info):
        _tile, tank = tank_info
        x, y = _tile
        new_x = x+1
        if new_x < self.width:
            _tile = (new_x, y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return tank_info
