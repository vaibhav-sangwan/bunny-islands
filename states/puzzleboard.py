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
from components.boardbutton import BoardButton
from components.tilecontroller import TileController


class PuzzleBoard:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load("./assets/bg.png")
        self.bg_rect = self.bg.get_rect(topleft=(0, 0))
        self.reset()

    def reset(self):
        self.tile_controller = TileController()
        self.grid = Grid(272, 16, self.tile_controller)

        self.tiles = [
            Tile("./assets/tile-1.png",
            [
                "WWLL",
                "WLLL",
                "LLLW",
                "LRWW",
                "LLWW",
                "LWWW",
                "WWWL",
                "WWLL"
            ],
            320, 32
            ),

            Tile("./assets/tile-2.png",
            [
                "LLWW",
                "LLLW",
                "WWLL",
                "WWLL",
                "WWBL",
                "WWLL",
                "LLLW",
                "LLWW"
            ],
            320, 112
            ),

            Tile("./assets/tile-3.png",
            [
                "WWLL",
                "WWWL",
                "LLWW",
                "LLWW",
                "RLWW",
                "LLWW",
                "WWWL",
                "WWLL"
            ],
            320, 192
            ),

            Tile("./assets/tile-4.png",
            [
                "LLWW",
                "LLLW",
                "WLLL",
                "WWLL",
                "WWRL",
                "WWLL",
                "LWWW",
                "LLWW"
            ],
            320, 272
            ),

            Tile("./assets/tile-5.png",
            [
                "LLWW",
                "LWWW",
                "WWLL",
                "WWLL",
                "WLBL",
                "WLLL",
                "LLWW",
                "LLWW"
            ],
            320, 352
            ),

            Tile("./assets/tile-6.png",
            [
                "LLWW",
                "LLLW",
                "WLLL",
                "WWLL",
                "WWBL",
                "WWLL",
                "LWWW",
                "LLWW"
            ],
            320, 432
            )
        ]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.tile_controller.handle_press()
            self.grid.handle_press()
            for tile in self.tiles:
                if tile.check_press():
                    self.tile_controller.select(tile)

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.grid.draw(self.screen)
        
        for tile in self.tiles:
            tile.draw(self.screen)
        
        self.tile_controller.draw(self.screen)

    def run(self):
        self.grid.update()
        self.tile_controller.update()
        
        for tile in self.tiles:
            tile.update()

        if len(self.grid.placed_tiles) == 6:
            won, snap, snap_rect = self.grid.check_win()
            self.gameStateManager.set_state("result-screen")
            result_state = self.game.states["result-screen"]
            result_state.won = won
            result_state.grid_snap = snap
            result_state.grid_snap_rect = snap_rect
            result_state.reset()

        self.render()
