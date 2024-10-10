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
from components.grid import Cell


class Tile(pygame.sprite.Sprite):
    def __init__(self, path, cell_status, top, left):
        super().__init__()

        self.path = path
        self.cell_status = cell_status
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(left, top))
        self.dims = (len(cell_status), len(cell_status[0]))
        self.tint_color = None

        self.cells = []
        for i in range(self.dims[0]):
            row = []
            for j in range(self.dims[1]):
                row.append(Cell(cell_status[i][j]))
            self.cells.append(row)
    
    def copy(self):
        clone = Tile(self.path, self.cell_status, self.rect.top, self.rect.left)
        clone.image = self.image.copy()
        clone.rect = self.rect.copy()
        clone.dims = self.dims
        clone.tint_color = self.tint_color
        clone.cells = self.cells
        return clone
    
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(self.rect.center))

        if angle == 90:
            self.cells = self.rotate_cells_clockwise()
        elif angle == -90:
            for _ in range(3):
                self.cells = self.rotate_cells_clockwise()

    def rotate_cells_clockwise(self):
        xt = []
        for j in range(len(self.cells[0])):
            col = []
            for i in range(len(self.cells) - 1, -1, -1):
                col.append(self.cells[i][j])
            xt.append(col)
        self.dims = (self.dims[1], self.dims[0])
        return xt        

    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.tint_color:
            overlay = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            pygame.draw.rect(overlay, self.tint_color, pygame.Rect(0, 0, self.rect.width, self.rect.height))
            screen.blit(overlay, self.rect)
    
    def update(self):
        pass
