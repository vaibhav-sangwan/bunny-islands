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
import random
import math


class Particles:
    def __init__(self, pos):
        self.particles = []
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.origin = pos
        self.add_particles(pos)

    def add_particles(self, pos):
        num_particles = 40
        for i in range(num_particles):
            radius = 2
            speed = random.uniform(12, 15)
            theta = random.uniform(0, 2 * math.pi)
            velocity = [speed * math.cos(theta), speed * math.sin(theta)]
            particle = [radius, [pos[0], pos[1]], velocity]
            self.particles.append(particle)

    def emit(self, screen):
        self.delete_particles()
        for particle in self.particles:
            particle[2][1] += 1.4
            particle[1][0] += particle[2][0]
            particle[1][1] += particle[2][1]
            if particle[1][1] > 100:
                particle[0] -= 0.01
            pygame.draw.circle(screen, self.color, particle[1], particle[0])

    def delete_particles(self):
        particles_copy = [
            particle for particle in self.particles if particle[1][1] < 480
        ]
        self.particles = particles_copy

    def done_emitting(self):
        return len(self.particles) == 0
