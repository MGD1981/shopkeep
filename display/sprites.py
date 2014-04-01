import pygame as pg
from pygame.locals import *
import reference_data as ref

class Shopkeep(pg.sprite.Sprite):
    """The player"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(ref.sprite_dct['player'],-1)
        self.pos = 0, 0

    def update(self):
        key_press = pg.key.get_pressed()
        if key_press[K_LEFT]:
            self.pos[0] -= 1
        if key_press[K_RIGHT]:
            self.pos[0] += 1
        if key_press[K_UP]:
            self.pos[1] -= 1
        if key_press[K_DOWN]:
            self.pos[1] += 1
