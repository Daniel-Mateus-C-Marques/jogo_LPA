#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.const import COLLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_USER
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
import pygame

from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = None
        self.window = window
        self.name = name
        self.game_mode = game_mode # MODO DE JOGO
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000 # 20 segundos
        if self.game_mode == MENU_OPTION[1] or self.game_mode == MENU_OPTION[2]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_USER, 4000)

    def run(self, ):
        pygame.mixer.music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        print(self.entity_list)
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_list.append(shot)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_USER:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, self.name, COLLOR_WHITE, (10,5))
            self.level_text(14,f'FPS: {clock.get_fps()}', COLLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidade: {len(self.entity_list)}', COLLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
