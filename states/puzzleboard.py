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



class PuzzleBoard:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def render(self):
        self.screen.fill("black")

    def run(self):
        self.render()
