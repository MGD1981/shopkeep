import os, sys
import pygame as pg
from pygame.locals import *
from data import entities, reference_data as ref

def load_image(name, colorkey=None):
    try:
        image = pg.image.load(name)
    except pg.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Person(pg.sprite.Sprite):
    """The player"""
    def __init__(self, img, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img, -1)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = x, y

    def update(self, game):
        if game.keys[K_LEFT]:
            entities.player['object'].location[0] -= 1
            self.rect = self.rect.move(-1,0)
        if game.keys[K_RIGHT]:
            entities.player['object'].location[0] += 1
            self.rect = self.rect.move(1,0)
        if game.keys[K_UP]:
            entities.player['object'].location[1] -= 1
            self.rect = self.rect.move(0,-1)
        if game.keys[K_DOWN]:
            entities.player['object'].location[1] += 1
            self.rect = self.rect.move(0,1)
        


class BackgroundTile(pg.sprite.Sprite):
    """Background tiles"""
    def __init__(self, img, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img, -1)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = x, y
