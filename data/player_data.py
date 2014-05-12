import random
import entities
import display
import reference_data as ref
import pygame as pg
from pygame.locals import *

class Player():
    """Player object"""
    def __init__(self):
        self.location = [ref.initial_player_position[0] * ref.tile_size,
                         ref.initial_player_position[1] * ref.tile_size]
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
    

