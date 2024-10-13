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

from utils import Utils
red = (172, 50, 50, 150)
green = (106, 190, 48, 150)

grid_status = [
    "EEEEEEEEEEEEEEEEEEEEEE",
    "ELLLLWWWWLLLLWWWWLLLLE",
    "ELLLLWWWWLLLLWWWWLLLLE",
    "ELLEEEEEEEEEEEEEEEELLE",
    "ELLEEEEEEEEEEEEEEEELLE",
    "EWWEEEEEEEEEEEEEEEEWWE",
    "EWWEEEEEEEEEEEEEEEEWWE",
    "EWWEEEEEEEEEEEEEEEEWWE",
    "EWWEEEEEEEEEEEEEEEEWWE",
    "ELLEEEEEEEEEEEEEEEELLE",
    "ELLEEEEEEEEEEEEEEEELLE",
    "ELLEEEEEEEEEEEEEEEELLE",
    "ELLEEEEEEEEEEEEEEEELLE",
    "EWWEEEEEEEEEEEEEEEEWWE",
    "EWWEEEEEEEEEEEEEEEEWWE",
    "EWWWWLLLLWWWWLLLLWWWWE",
    "EWWWWLLLLWWWWLLLLWWWWE",
    "EEEEEEEEEEEEEEEEEEEEEE"
]


class Grid(pygame.sprite.Sprite):
    def __init__(self, x, y, controller):
        super().__init__()
        self.dims = (18, 22)
        self.cells = []
        for i in range(self.dims[0]):
            row = []
            for j in range(self.dims[1]):
                row.append(Cell(grid_status[i][j]))
            self.cells.append(row)

        self.image = pygame.image.load("./assets/grid.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.controller = controller

        self.held_tile = None
        self.placed_tiles = []

    def print_grid(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                print(self.cells[i][j].status, end=" ")
            print()
        print("\n")

    def fill_cells(self, tile):
        r, c, m, n = self.get_indices(tile)

        for i in range(m):
            for j in range(n):
                self.cells[r + i][c + j].status = tile.cells[i][j].status

    def place_tile(self, tile):
        self.controller.tile.rect = tile.rect.copy()
        self.controller.tile.tint_color = None
        self.fill_cells(tile)
        self.placed_tiles.append(self.controller.tile)
        self.controller.tile = None
        self.held_tile = None

    def get_indices(self, tile):
        r = ((tile.rect.top // 16) - (self.rect.top // 16))
        c = ((tile.rect.left // 16) - (self.rect.left // 16))
        m, n = tile.dims

        return r, c, m, n

    def clear_cells(self, tile):
        r, c, m, n = self.get_indices(tile)

        for i in range(m):
            for j in range(n):
                self.cells[r + i][c + j].status = "E"

    def handle_press(self):
        if not self.held_tile:
            i = 0
            while i < len(self.placed_tiles):
                tile = self.placed_tiles[i]
                if tile.check_press():
                    self.placed_tiles.pop(i)
                    self.clear_cells(tile)
                    self.controller.select(tile, copy=False)
                else:
                    i += 1

        if self.held_tile and self.is_placeable(self.held_tile):
            self.place_tile(self.held_tile)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for tile in self.placed_tiles:
            tile.draw(screen)
        if self.held_tile:
            self.held_tile.draw(screen)
    
    def snap_tile(self, tile):
        tile.rect.center = Utils.norm_cursor_pos()
        top = (tile.rect.top // 32) * 32
        left = (tile.rect.left // 32) * 32
        return top, left

    def grid_empty(self, r, c, m, n):
        for i in range(r, r + m):
            for j in range(c, c + n):
                if i < 0 or j < 0 or i >= len(self.cells) or j >= len(self.cells[0]) or self.cells[i][j].status != "E":
                    return False
        return True

    def is_placeable(self, tile):
        m, n = tile.dims
        i = ((tile.rect.top // 16) - (self.rect.top // 16))
        j = ((tile.rect.left // 16) - (self.rect.left // 16))
        return self.grid_empty(i, j, m, n)
    
    def update(self):
        cursor_pos = Utils.norm_cursor_pos()
        if self.rect.collidepoint(cursor_pos) and self.controller.tile:
            if not self.held_tile:
                self.held_tile = self.controller.tile.copy()
            top, left = self.snap_tile(self.held_tile)
            self.held_tile.rect.topleft = (left, top)
            if self.is_placeable(self.held_tile):
                self.held_tile.tint_color = green
            else:
                self.held_tile.tint_color = red
        else:
            self.held_tile = None

        if not self.held_tile:
            for tile in self.placed_tiles:
                if tile.check_press():
                    tile.tint_color = green
                else:
                    tile.tint_color = None
   
class Cell:
    def __init__(self, status):
        self.status = status

    def is_empty(self):
        return self.status == "E"
