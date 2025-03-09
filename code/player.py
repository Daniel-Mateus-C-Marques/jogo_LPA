#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[MOVE_UP[self.name]] and self.rect.centery > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[MOVE_DOWN[self.name]] and self.rect.centery < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[MOVE_LEFT[self.name]] and self.rect.centerx > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[MOVE_RIGHT[self.name]] and self.rect.centerx < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
