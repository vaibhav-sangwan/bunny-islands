#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Bunny Islands
# Copyright (C) 2024 Vaibhav Sangwan
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
#
# Contact information:
# Vaibhav Sangwan    sangwanvaibhav02@gmail.com

import pygame

from components.grid import Grid
from components.tile import Tile


class PuzzleBoard:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.grid = Grid(272, 16)
        self.tile_list = [
            Tile("./assets/tile-1.png", []),
            Tile("./assets/tile-2.png", []),
            Tile("./assets/tile-3.png", []),
            Tile("./assets/tile-4.png", []),
            Tile("./assets/tile-5.png", []),
            Tile("./assets/tile-6.png", []),
        ]

        self.focused_tile = None
        self.prev = ""

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in self.tile_list:
                if tile.check_press():
                    self.focused_tile = tile
                    tile.focus()
                elif tile.focused:
                    tile.unfocus()
            if self.grid.handle_press(self.focused_tile):
                self.focused_tile = None
        elif event.type == pygame.KEYDOWN:
            if self.focused_tile:
                if self.focused_tile.placed:
                    if event.key == pygame.K_d:
                        self.focused_tile.placed = False
                        self.focused_tile = None
                else:
                    if event.key == pygame.K_RIGHT:
                        self.focused_tile.rotate(-90)
                    elif event.key == pygame.K_LEFT:
                        self.focused_tile.rotate(90)

    def render(self):
        self.screen.fill("white")
        self.grid.draw(self.screen)
        
        for tile in self.tile_list:
            tile.draw(self.screen)

    def run(self):
        self.grid.update(self.focused_tile)

        inactive = 0
        for tile in self.tile_list:
            tile.update()
            if not tile.focused and not tile.placed:
                tile.rect.left = 16 + (inactive * 80)
                tile.rect.top = 320
                inactive += 1
        self.render()
