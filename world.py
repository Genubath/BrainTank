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

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QWidget


class Tile(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)


class DirtTile(Tile):
    def __init__(self):
        Tile.__init__(self)
        self.setPixmap(QPixmap("PlanetCute/Dirt_Block.png"))


class GrassTile(Tile):
    def __init__(self):
        Tile.__init__(self)
        self.setPixmap(QPixmap("PlanetCute/Grass_Block.png"))


class World(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

    def paintEvent(self, paint_event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.render_map_background(painter)

        tank = QPixmap("tank/blue_up.png")
        painter.drawPixmap(303, 77, tank)

    @staticmethod
    def render_map_background(painter):
        pixmap = QPixmap("PlanetCute/Grass_Block.png")
        painter.drawPixmap(0, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 0, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 0, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 77, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 77, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 154, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 154, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 231, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 231, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 308, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 308, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 385, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 385, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 462, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 462, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 539, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 539, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 616, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 616, pixmap, 0, 55, 101, 77)

        painter.drawPixmap(0, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(101, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(202, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(303, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(404, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(505, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(606, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(707, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(808, 693, pixmap, 0, 55, 101, 77)
        painter.drawPixmap(909, 693, pixmap, 0, 55, 101, 77)



#    def play_music(self):
#        self.main_music.play()
#
#    def generate_map(self):
#        self.__map = [[(self.grass, None)]*self.width for x in range(self.height)]
#
#        def distmap(pairs):
#            return [i for sublist in [[x]*y for x,y in pairs] for i in sublist]
#
#        # spawn lists
#        terrain = distmap(((self.grass, 20), (self.dirt, 5), (self.water, 1)))
#        items = distmap(((None, 20), (self.rock,2), (self.tree,2)))
#
#        # generate actual map
#        r = self.rand
#        for row in self.__map:
#            for i in range(len(row)):
#                tile = r.choice(terrain)
#                item = None
#                if tile in self.safe: # avoid water etc for placeables
#                    item = r.choice(items)
#
#                row[i] = (tile, item)
#
#        self.ITEM_TO_ENUM.update({
#            None:      None,
#            self.rock: Item.ROCK,
#            self.tree: Item.TREE,
#        })
#
#        self.TILE_TO_ENUM.update({
#            None:       None,
#            self.grass: Tile.GRASS,
#            self.dirt:  Tile.DIRT,
#            self.plain: Tile.PLAIN,
#            self.water: Tile.WATER,
#        })
#
#    def add_tanks(self, tank_colors):
#        s1 = (0, 0, Facing.RIGHT)
#        s2 = (0, self.height-1, Facing.UP)
#        s3 = (self.width-1, self.height-1, Facing.LEFT)
#        s4 = (self.width-1, 0, Facing.DOWN)
#
#        spawns = self.rand.sample((s1,s2,s3,s4), len(tank_colors))
#
#        self.tanks = []
#        for spawn,color in zip(spawns, tank_colors):
#            tank = Tank(self, spawn[0], spawn[1], spawn[2], color)
#            self.__set_tile(spawn, (self.plain, tank))
#            self.tanks.append(tank)
#
#        self.ITEM_TO_ENUM.update({
#            x: x.color.upper() for x in self.tanks
#        })
#
#    def __set_tile(self, pos, data):
#        #print "setting", pos, data
#        self.__map[pos[1]][pos[0]] = data
#
#    def world_to_screen(self, x, y):
#        '''Convert tile coordinates to screen pixel coordinates'''
#        x = self.start_x + x * self.tile_size[0]
#        y = self.start_y + (y-1) * self.tile_size[1]
#        return (x,y)
#
#    def screen_to_world(self, x, y):
#        '''Convert screen pixel coordinates to tile coordinates'''
#        x = (x - self.start_x) * self.tile_size_inv[0]
#        y = (y - self.start_y) * self.tile_size_inv[1] + 1
#        return (int(x),int(y))
#
#    def draw(self):
#        gl.glEnable(gl.GL_BLEND)
#        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
#        gl.glEnable(gl.GL_DEPTH_TEST)
#        gl.glDepthFunc(gl.GL_LEQUAL)
#
#        dx = self.tile_size[0]
#        dy = self.tile_size[1]
#        stack = self.half_stack
#
#        # terrain pass
#        x, y = self.start_x, self.start_y
#        for row in self.__map:
#            x = self.start_x
#            for tile,item in row:
#                tile.blit(x,y,0)
#                x += dx
#            y += dy
#
#        # bullet pass
#
#        for bullet in self.bullets:
#            bullet.draw()
#
#        # item pass
#        x, y = self.start_x, self.start_y
#        for row in self.__map:
#            x = self.start_x
#            for tile,item in row:
#                if item is not None:
#                    item.blit(x,y+stack,1)
#                x += dx
#            y += dy
#
#    def warp(self, tank):
#        '''Called before tank sets x,y to new tile.'''
#        pos = tank.get_position()
#        wpos = tank.get_warp_destination()
#
#        src = self.get_tile(pos[0], pos[1])
#        dst = self.get_tile(wpos[0], wpos[1])
#        if dst[0] not in self.safe and tank.brain:
#            tank.brain.kill()
#            return
#
#        self.__set_tile(pos, (src[0], None))
#        self.__set_tile(wpos, (dst[0], tank))
#
#    def update(self, dt):
#        dead_expl = []
#        for explosion in self.explosions:
#            explosion.update(dt)
#            if not explosion.is_exploding():
#                dead_expl.append(explosion)
#        for explosion in dead_expl:
#            self.explosions.remove(explosion)
#
#        if not self.game_over:
#            # update bullets
#            dead_bullets = []
#            for bullet in self.bullets:
#                bullet.update(dt)
#                x,y = self.screen_to_world(bullet.x, bullet.y)
#                tile, item = self.get_tile(x,y)
#                #print "bullet at", x, y, "facing", bullet.facing
#                if x < 0 or y < 0 or x >= self.width or y >= self.height:
#                    dead_bullets.append(bullet)
#                elif item in self.destructible:
#                    self.detonate(item, pos=(x,y))
#                    dead_bullets.append(bullet)
#                #else:
#                    #self.__set_tile((x,y), (tile, self.spawn))
#
#            for bullet in dead_bullets:
#                self.bullets.remove(bullet)
#                bullet.tank.bullet = None # bleh
#                self.detonate(bullet)
#
#            # update tanks
#            tanks = list(self.tanks)
#            self.rand.shuffle(tanks)
#
#            for tank in tanks:
#                tank.update(dt)
#
#                # check for tank collision w/ bullets
#                # slow but i'm in a hurry and it's python anyway lol
#                trect = tank.rect()
#
#                for bullet in self.bullets:
#                    #print "checking", tank.color, "against", bullet.tank.color, "'s bullet"
#                    if bullet.tank is not tank and bullet.rect().touches(trect):
#                        tank.kill()
#                        self.detonate(tank)
#
#    def detonate(self, thing, pos=None):
#        '''Detonate (destroy) an object on the map, optionally clearing the item at pos'''
#
#        if config.DEBUG:
#            print "blowing up", thing
#
#        if thing in self.tanks:
#            print "GAME OVER!"
#            self.game_over = True
#
#        if pos:
#            tile, item = self.get_tile(pos[0], pos[1])
#            self.__set_tile(pos, (tile, None))
#
#    def add_bullet(self, bullet):
#        self.bullets.append(bullet)
#
