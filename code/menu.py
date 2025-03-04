#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import COLLOR_ORANGE, WIN_WIDTH, MENU_OPTION, COLLOR_WHITE, COLLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load('./assets/Menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            #DRAW IMAGES
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, 'Mountain', COLLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLLOR_YELLOW, ((WIN_WIDTH / 2), 180 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))

            pygame.display.flip()

            # for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # TECLA DOWN
                        if menu_option == len(MENU_OPTION) - 1:
                            menu_option = 0
                        else:
                            menu_option += 1
                    if event.key == pygame.K_UP: #TECLA UP
                        if menu_option == 0:
                            menu_option = len(MENU_OPTION) - 1
                        else:
                            menu_option -= 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
