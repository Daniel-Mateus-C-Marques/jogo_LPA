import pygame
from pygame import K_w, K_UP, K_DOWN, K_s, K_LEFT, K_a, K_d, K_RIGHT

WIN_WIDTH = 576
WIN_HEIGHT = 324
COLLOR_ORANGE = (255, 128, 0)
COLLOR_WHITE = (255, 255, 255)
COLLOR_YELLOW = (255, 255, 0)

MENU_OPTION = ('NEW GAME',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

EVENT_USER = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 3
}

MOVE_UP = {'Player1': K_UP, 'Player2': K_w}
MOVE_DOWN = {'Player1': K_DOWN, 'Player2': K_s}
MOVE_LEFT = {'Player1': K_LEFT, 'Player2': K_a}
MOVE_RIGHT = {'Player1': K_RIGHT, 'Player2': K_d}
