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

from components.particles import Particles
from components.boardbutton import BoardButton


class ResultScreen:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load("./assets/bg.png")
        self.bg_rect = self.bg.get_rect(topleft=(0, 0))

        self.lost_img = pygame.image.load("./assets/lost.png")
        self.lost_img_rect = self.lost_img.get_rect(center = (self.screen.get_width()/2, 382))
        self.won_img = pygame.image.load("./assets/won.png")
        self.won_img_rect = self.won_img.get_rect(center = (self.screen.get_width()/2, 382))

        self.home_button = BoardButton(
            self.won_img_rect.right + 32, 382,
            './assets/home-button-pressed.png',
            './assets/home-button-unpressed.png'
        )

        self.won = None
        self.grid_snap = None
        self.grid_snap_rect = None
        self.status_img = None
        self.status_img_rect = None
        self.particles = None

    def reset(self):
        self.grid_snap_rect.center = (
            self.screen.get_width()/2,
            self.screen.get_height()/2 - 32
        )
        if self.won:
            self.status_img = self.won_img
            self.status_img_rect = self.won_img_rect
            self.particles = [
                Particles( 
                    (
                        self.grid_snap_rect.left + 48 + (i * 32),
                        self.grid_snap_rect.top
                    )
                ) for i in range(9)
            ]
        else:
            self.status_img = self.lost_img
            self.status_img_rect = self.lost_img_rect
            self.particles = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.home_button.check_press():
                self.gameStateManager.set_state("puzzle-board")
                board_state = self.game.states["puzzle-board"]
                board_state.reset()

    def render(self):
        self.screen.fill("white")
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.grid_snap, self.grid_snap_rect)
        self.screen.blit(self.status_img, self.status_img_rect)
        self.screen.blit(self.home_button.image, self.home_button.rect)
        for particle in self.particles:
            if not particle.done_emitting():
                particle.emit(self.screen)

    def run(self):
        self.home_button.update()
        self.render()
