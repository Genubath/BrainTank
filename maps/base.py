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
        print("update map")
        # for each tank check to see if it has an action
        # if it does... update it... if not ask for another action
        for tank_info in self._tanks:
            _id, _x, _y, tank = tank_info
            if tank.state is state.TANK_IDLE:
                _action = tank.get_next_action()
                action = command.command_to_string(_action)
                print("Tank [%s] is taking action %s" % (tank.name, action))

        # for each projectile... update it...
        for boom in self._projectiles:
            pass

        self.world.update()
