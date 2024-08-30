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


class Tile(pygame.sprite.Sprite):
    def __init__(self, path, edges):
        super().__init__()

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.edges = edges
        
        self.focused = False
        self.placed = False
        self.hover_effect = False

        self.rotated_by = 0
    
    def unfocus(self):
        self.focused = False
        self.hover_effect = False
        if self.focused and not self.placed:
            self.image = pygame.transform.rotate(self.image, -self.rotated_by)
            self.rect = self.image.get_rect()
            self.rotated_by = 0
    
    def place(self, rect):
        self.rect = rect.copy()
        self.placed = True
        self.focused = False
        self.hover_effect = False
        self.unfocus()
    
    def focus(self):
        if not self.placed and not self.focused:
            self.rect.centerx = 160
            self.rect.centery = 176
            
        self.focused = True
        self.hover_effect = True
    
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(self.rect.center))
        self.rotated_by += angle
    
    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.hover_effect:
            hover_rect = pygame.Rect(self.rect.left - 2, self.rect.top - 2, self.rect.width + 4, self.rect.height + 4)
            pygame.draw.rect(screen, "black", hover_rect, 1)
    
    def update(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            self.hover_effect = True
        elif not (self.focused and self.placed):
            self.hover_effect = False
