import pygame
from pygame import K_w, K_UP, K_DOWN, K_s, K_LEFT, K_a, K_d, K_RIGHT, K_RCTRL, K_LCTRL

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

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 40,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 110,
    'Enemy2': 100,

}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 2,
    'Enemy1Shot': 6,
    'Enemy2': 3,
    'Enemy2Shot': 6
}

MOVE_UP = {'Player1': K_UP,
           'Player2': K_w}
MOVE_DOWN = {'Player1': K_DOWN,
             'Player2': K_s}
MOVE_LEFT = {'Player1': K_LEFT,
             'Player2': K_a}
MOVE_RIGHT = {'Player1': K_RIGHT,
              'Player2': K_d}
PLAYER_KEY_SHOT = {'Player1': K_RCTRL,
                   'Player2': K_LCTRL}
