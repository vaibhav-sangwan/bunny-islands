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

from components.boardbutton import BoardButton
from utils import Utils

class TileController:
    def __init__(self):
        self.del_button = BoardButton(160, 272, './assets/delete-button-pressed.png', './assets/delete-button-unpressed.png')
        self.rotclock_button = BoardButton(210, 272, './assets/rotclock-button-pressed.png', './assets/rotclock-button-unpressed.png')
        self.rotaclock_button = BoardButton(110, 272, './assets/rotaclock-button-pressed.png', './assets/rotaclock-button-unpressed.png')

        self.buttons = [self.del_button, self.rotclock_button, self.rotaclock_button]
        self.tile = None

    def handle_press(self):
        if self.del_button.check_press():
            self.unselect()
        if self.tile and self.rotclock_button.check_press():
            self.tile.rotate(90)
        if self.tile and self.rotaclock_button.check_press():
            self.tile.rotate(-90)

    def select(self, tile, copy=True):
        self.unselect()
        if copy:
            self.tile = tile.copy()
            self.tile.parent.visible = False
        else:
            self.tile = tile
        self.tile.rect.midtop = (160, 96)

    def unselect(self):
        if self.tile and self.tile.parent:
            self.tile.parent.visible = True
        self.tile = None

    def draw(self, screen):
        for button in self.buttons:
            screen.blit(button.image, button.rect)
        if self.tile:
            screen.blit(self.tile.image, self.tile.rect)

    def update(self):
        for button in self.buttons:
            button.update()
