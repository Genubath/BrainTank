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
from vehicle import Bullet


class BaseMap(AbstractMap):

    @pyqtSlot()
    def update(self):
        # for each projectile... update it...
        bullets_to_delete = []
        tanks_to_delete = []
        for _id, bullet_info in self._projectiles.items():
            _tile, bullet = bullet_info

            # mark the bullet for destruction if it has already reached the edge
            _x, _y = _tile
            if _x == 0 or _x == self.width-1 or _y == 0 or _y == self.height-1:
                bullets_to_delete.append(_id)
            else:
                _updated_info = self.move_it(command.MOVE_FORWARD, bullet_info)
                self._projectiles[_id] = _updated_info
                # now that the bullet is updated we need to see if it killed any tank
                for _tank_id, tank_info in self._tanks.items():
                    _tank_tile, _tank = tank_info
                    _tank_x, _tank_y = _tank_tile
                    if _x == _tank_x and _y == _tank_y:
                        # boom... hopefully it's not a dud
                        if bullet.fired_by != _tank_id:
                            tanks_to_delete.append(_tank_id)
                            _destroyer_id, _destroyer = self._tanks[bullet.fired_by]
                            print("BOOM!!! %s was destroyed by %s!" % (_tank.name, _destroyer.name))

        # delete bullets and tanks that were scheduled to be destroyed because this can't be done in the loop
        for id in bullets_to_delete:
            del self._projectiles[id]

        for id in tanks_to_delete:
            del self._tanks[id]

        # for each tank check to see if it has an action
        # if it does... update it... if not ask for another action
        for _id, tank_info in self._tanks.items():
            _tile, tank = tank_info
            if tank.state is state.TANK_IDLE:
                _action = tank.get_next_action()
                _updated_info = self.move_it(_action, tank_info, _id)
                self._tanks[_id] = _updated_info

        self.world.update()

    def move_it(self, _action, _info: tuple, _id=None):
        _tile, obj, = _info

        # move forward
        if _action == command.MOVE_FORWARD:
            return self.move_forward(_info)

        # move backward
        elif _action == command.MOVE_BACKWARD:
            return self.move_backward(_info)

        # turn left
        elif _action == command.TURN_LEFT:
            if obj.facing == state.FACING_RIGHT:
                obj.facing = state.FACING_UP
            elif obj.facing == state.FACING_DOWN:
                obj.facing = state.FACING_RIGHT
            elif obj.facing == state.FACING_LEFT:
                obj.facing = state.FACING_DOWN
            elif obj.facing == state.FACING_UP:
                obj.facing = state.FACING_LEFT

        # turn right
        elif _action == command.TURN_RIGHT:
            if obj.facing == state.FACING_RIGHT:
                obj.facing = state.FACING_DOWN
            elif obj.facing == state.FACING_DOWN:
                obj.facing = state.FACING_LEFT
            elif obj.facing == state.FACING_LEFT:
                obj.facing = state.FACING_UP
            elif obj.facing == state.FACING_UP:
                obj.facing = state.FACING_RIGHT

        # turn around
        elif _action == command.TURN_AROUND:
            if obj.facing == state.FACING_RIGHT:
                obj.facing = state.FACING_LEFT
            elif obj.facing == state.FACING_LEFT:
                obj.facing = state.FACING_RIGHT
            elif obj.facing == state.FACING_DOWN:
                obj.facing = state.FACING_UP
            elif obj.facing == state.FACING_UP:
                obj.facing = state.FACING_DOWN
            else:
                # this should never happen... restoring sanity to the world
                obj.facing = state.FACING_RIGHT
            return _tile, obj

        # shoot
        elif _action == command.SHOOT:
            bullet = Bullet(_id, obj.facing)
            self.add_projectile(bullet, _tile)

        # something bad happened
        else:
            print("Object [%s] issued unknown action %s" % (obj.name, _action))
        return _info

    def move_forward(self, _info):
        _tile, tank = _info
        if tank.facing == state.FACING_RIGHT:
            return self.move_right(_info)
        elif tank.facing == state.FACING_LEFT:
            return self.move_left(_info)
        elif tank.facing == state.FACING_UP:
            return self.move_up(_info)
        elif tank.facing == state.FACING_DOWN:
            return self.move_down(_info)
        return _info

    def move_backward(self, _info):
        _tile, tank = _info
        if tank.facing == state.FACING_RIGHT:
            return self.move_left(_info)
        elif tank.facing == state.FACING_LEFT:
            return self.move_right(_info)
        elif tank.facing == state.FACING_UP:
            return self.move_down(_info)
        elif tank.facing == state.FACING_DOWN:
            return self.move_up(_info)
        return _info

    def move_up(self, _info):
        _tile, tank = _info
        x, y = _tile
        new_y = y-1
        if new_y >= 0:
            _tile = (x, new_y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return _info

    def move_down(self, _info):
        _tile, tank = _info
        x, y = _tile
        new_y = y+1
        if new_y < self.height:
            _tile = (x, new_y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return _info

    def move_left(self, _info):
        _tile, tank = _info
        x, y = _tile
        new_x = x-1
        if new_x >= 0:
            _tile = (new_x, y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return _info

    def move_right(self, _info):
        _tile, tank = _info
        x, y = _tile
        new_x = x+1
        if new_x < self.width:
            _tile = (new_x, y)
            return _tile, tank
        # just return the original info so that we don't move if we've hit the edge
        return _info
