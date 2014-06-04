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
    

    def tick(self):
        if (len(entities.shop['object'].transaction_queue) > 0 and 
            self.get_shop_tile() == 'cashier'
        ):
            self.transact(entities.shop['object'].transaction_queue[0])

    def transact(self, hero):
        print "Transaction!"
        #TODO

    def get_shop_tile(self):
        return ref.shop_tile_dct[entities.shop['object'].shop_grid[
            self.location[1]/ref.tile_size][self.location[0]/ref.tile_size]
            ]['tile type']

