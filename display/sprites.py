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
    image = image.convert_alpha()
    image = pg.transform.scale(image, (int(image.get_width()*ref.scale), 
                                       int(image.get_height()*ref.scale)))
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0)) #gets transparent colorkey
        image.set_colorkey(colorkey, RLEACCEL)
    return image


class Person(pg.sprite.Sprite):
    """The player"""
    def __init__(self, game, img_list, x, y):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        for image in img_list:
            self.images.append(load_image(ref.image_path + image, -1))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.blink = False

    def update(self, game):
        if game.keys[K_LEFT]:
            if self.validate(0,-1):
                self.move(0,-1)
                self.refresh(game)
        if game.keys[K_RIGHT]:
            if self.validate(0,1):
                self.move(0,1)
                self.refresh(game)
        if game.keys[K_UP]:
            if self.validate(1,-1):
                self.move(1,-1)
                self.refresh(game)
        if game.keys[K_DOWN]:
            if self.validate(1,1):
                self.move(1,1)
                self.refresh(game)

    def refresh(self, game):
        if game.blink != self.blink:
            self.blink = game.blink
            self.animate()
        game.action_log.append('refresh background')

    def animate(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
    def validate(self, axis, direction):
        #axis: 0=x, 1=y
        #direction: 1=right, down  -1=left, up
        vector = ref.player_speed * direction

        #TODO: Use native pygame sprite collision detection
        #      by creating two kinds of sprite groups:
        #      one passable and one not passable

        try:
            for sprite_border in [
                (0,0),
                (1,0),
                (1,1),
                (0,1)
                                 ]:
                if not ref.shop_tile_dct[
                    entities.shop['object'].shop_grid[
                        ((entities.player['object'].location[1] + 
                        (sprite_border[1] * (self.rect.height-1))) + 
                        axis*vector)/ref.tile_size][
                        ((entities.player['object'].location[0] + 
                        (sprite_border[0] * (self.rect.width-1))) + 
                        (-axis+1)*vector)/ref.tile_size]]['passable'
                ]:
                    return False
            return True
        except IndexError:
            return False 


    def move(self, axis, direction):
        vector = ref.player_speed * direction
        entities.player['object'].location[axis] += vector
        self.rect = self.rect.move((-axis+1)*vector, axis*vector)


class BackgroundTile(pg.sprite.Sprite):
    """Background tiles"""
    def __init__(self, game, img, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image(img, -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y


class Button(pg.sprite.Sprite):
    """Menu buttons"""
    def __init__(self, game, name, img, x, y):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.image = load_image(img, -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.mouse_on = False
        self.clicked = False

    def update(self, game):
        mouse_presses = pg.mouse.get_pressed()
        if self.mouse_on == True and mouse_presses[0] and not self.clicked:
            self.clicked = True
            game.action_log.extend([
                '%s view' % self.name,
                'refresh background'
            ])
        if self.rect.collidepoint(game.mouse_pos):
            self.mouse_on = True
            pg.draw.rect(
                game.screens['banner'].background,
                ref.primary_color,
                self.rect,
                1
            )
        elif self.mouse_on == True:
            self.mouse_on = False
            self.clicked = False
            pg.draw.rect(
                game.screens['banner'].background,
                ref.background_color,
                self.rect,
                1
            )
                
