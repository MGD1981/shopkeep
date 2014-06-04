import os, sys
import pygame as pg
from pygame.locals import *
from data import entities, reference_data as ref
from random import randint
from math import copysign
import copy

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
    """People in the shop super-class"""
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
        pass

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
        
    def validate(self, game, axis, direction):
        vector = ref.player_speed * direction
        test_sprite = pg.sprite.Sprite()
        test_sprite.rect = copy.deepcopy(self.rect)
        test_sprite.rect[0] = test_sprite.rect[0] + (-axis+1)*vector
        test_sprite.rect[3] = test_sprite.rect[3]/2
        test_sprite.rect[1] = test_sprite.rect[1] + test_sprite.rect[3] + axis*vector
        if not game.screens['world'].background.get_rect().contains(test_sprite.rect):
            return False
        if len(pg.sprite.spritecollide(test_sprite, game.screens['world'].impassable_shop_tiles, False)) > 0:
            return False
        return True

    def move(self, axis, direction, origin=None):
        """Moves sprite's rect in a direction an amount equal to ref.player_speed:
        axis: 0 for x-axis, 1 for y-axis
        direction: 1 for forward, -1 for backward
        """
        vector = ref.player_speed * direction
        if origin != None:
            origin[axis] += vector
        self.rect = self.rect.move((-axis+1)*vector, axis*vector)


class Player(Person):
    """Player-controlled shopkeep in the shop"""
    def __init__(self, game, img_list, x, y):
        super(Player, self).__init__(game, img_list, x, y)

    def update(self, game):
        origin = entities.player['object'].location
        if game.keys[K_LEFT]:
            if self.validate(game, 0,-1):
                self.move(0,-1, origin)
                self.refresh(game)
        if game.keys[K_RIGHT]:
            if self.validate(game, 0,1):
                self.move(0,1, origin)
                self.refresh(game)
        if game.keys[K_UP]:
            if self.validate(game, 1,-1):
                self.move(1,-1, origin)
                self.refresh(game)
        if game.keys[K_DOWN]:
            if self.validate(game, 1,1):
                self.move(1,1, origin)
                self.refresh(game)

class Hero(Person):
    """Heroes in the shop"""
    def __init__(self, hero_id, game, img_list, x, y):
        super(Hero, self).__init__(game, img_list, x, y)
        self.hero = [h for h in entities.heroes['object list'] if h.hero_id == hero_id][0]
        self.next_goal = None #coordinates of current path index

    def update(self, game):
        if self.next_goal == None:
            if self.hero.path != None:
                try:
                    self.next_goal = map(lambda x: x*ref.tile_size, (next(self.hero.path)))
                except StopIteration:
                    self.hero.pathfinder = None
                    self.hero.path = None
                    self.hero.shop_destination = None
                    self.next_goal = None
        else:
            origin = self.hero.shop_location
            if origin[0] != self.next_goal[0] and randint(1,3) != 3:
                axis = 0
                direction = int(copysign(1, self.next_goal[0] - origin[0]))
                if self.validate(game, axis, direction):
                    self.move(axis, direction, origin)
            if origin[1] != self.next_goal[1] and randint(1,3) != 3:
                axis = 1
                direction = int(copysign(1, self.next_goal[1] - origin[1]))
                if self.validate(game, axis, direction):
                    self.move(axis, direction, origin)
            self.rect[0] = self.hero.shop_location[0]
            self.rect[1] = self.hero.shop_location[1]
            if self.hero.shop_location == self.next_goal:
                self.next_goal = None
            self.refresh(game)
                
                

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
                
