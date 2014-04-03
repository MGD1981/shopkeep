import random
import entities
import pygame as pg
from pygame.locals import *

class Player():
    """Player object"""
    def __init__(self):
        self.location = [0, 0]
        self.coins = {
            'copper': 0,
            'silver': 0,
            'gold': 0
        }
        self.appraisal_skill = {
            'wood': 0,
            'fiber': 0,
            'stone': 0,
            'leather': 0,
            'metal': 0
        }
    


    def tick(self, game):
        key_press = pg.key.get_pressed()
        if key_press[K_LEFT]:
            self.location[0] -= 1
        if key_press[K_RIGHT]:
            self.location[0] += 1
        if key_press[K_UP]:
            self.location[1] -= 1
        if key_press[K_DOWN]:
            self.location[1] += 1
