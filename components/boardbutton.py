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


class BoardButton(pygame.sprite.Sprite):
    def __init__(self, x, y, pressed_path, unpressed_path):
        super().__init__()

        self.pressed_img = pygame.image.load(pressed_path)
        self.unpressed_img = pygame.image.load(unpressed_path)
        self.image = self.unpressed_img

        self.rect = self.image.get_rect(center=(x, y))
    
    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            return True
        return False

    def update(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()) and pygame.mouse.get_pressed()[0]:
            self.image = self.pressed_img
        else:
            self.image = self.unpressed_img
