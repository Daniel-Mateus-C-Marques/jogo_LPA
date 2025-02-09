import pygame as pg

pg.init()
print('Setup start')
window = pg.display.set_mode(size=(600, 480))

while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
           pg.quit() # Close window
           quit() # end pygame
