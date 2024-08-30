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


class Grid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("./assets/grid.png")
        self.rect = self.image.get_rect(topleft=(x, y))

        self.held_tile = None
        self.held_tile_rect = None

        self.cells = [
            [
                Cell() for j in range(22)
            ] for i in range(18)
        ]

        for i in range(18):
            for j in range(3):
                self.cells[i][j].occupied = True
                self.cells[i][-1 - j].occupied = True
        
        for j in range(22):
            for i in range(3):
                self.cells[i][j].occupied = True
                self.cells[-1 - i][j].occupied = True
    
    def place_tile(self, focused_tile, si, sj, ei, ej):
        for i in range(si, ei + 1):
            for j in range(sj, ej + 1):
                self.cells[j][i].occupied = True
        
        rect = pygame.Rect(self.rect.left + (si * 16), self.rect.top + (sj * 16), focused_tile.rect.width, focused_tile.rect.height)
        print("placing at", rect.topleft)
        focused_tile.place(rect)
        self.held_tile = None
        self.held_tile_rect = None
                
    
    def handle_press(self, focused_tile):
        if self.rect.collidepoint(Utils.norm_cursor_pos()) and focused_tile and not focused_tile.placed:
            si, sj, ei, ej = self.snap()
            if self.held_tile and self.check_placeability(si, sj, ei, ej):
                self.place_tile(focused_tile, si, sj, ei, ej)
                return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.held_tile:
            overlay_surf = pygame.Surface(self.held_tile.get_size(), pygame.SRCALPHA)
            overlay_surf.fill(self.overlay_color)
            self.held_tile.blit(overlay_surf, (0, 0))
            screen.blit(self.held_tile, self.held_tile_rect)

    
    def snap(self):
        sx, sy = self.held_tile_rect.topleft

        si = (sx - self.rect.left) // 16
        if si % 2 == 0 and si != 0:
            si -= 1

        sj = (sy - self.rect.top) // 16
        if sj % 2 == 0 and sj != 0:
            sj -= 1
        
        ei = si + (self.held_tile_rect.width // 16) - 1
        ej = sj + (self.held_tile_rect.height // 16) - 1

        if si >= 1 and sj >= 1 and ei < 21 and ej < 17:
            self.held_tile_rect.topleft = (self.rect.left + (16 * si), self.rect.top + (16 * sj))
        else:
            self.held_tile = None
            self.held_tile_rect = None
        
        return si, sj, ei, ej

    def check_placeability(self, si, sj, ei, ej):
        for i in range(si, ei + 1):
            for j in range(sj, ej + 1):
                if self.cells[j][i].occupied:
                    return False
        
        return True
    
    def update(self, focused_tile):
        mouse_pos = Utils.norm_cursor_pos()
        if self.rect.collidepoint(mouse_pos) and focused_tile:
            self.held_tile = focused_tile.image.copy()
            self.held_tile_rect = self.held_tile.get_rect(center=mouse_pos)
            si, sj, ei, ej = self.snap()
            if self.held_tile:
                if self.check_placeability(si, sj, ei, ej):
                    self.can_place = True
                    self.overlay_color = green
                else:
                    self.can_place = False
                    self.overlay_color = red
        else:
            self.held_tile = None
            self.held_tile_rect = None

            
class Cell:
    def __init__(self):
        self.occupied = False
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
