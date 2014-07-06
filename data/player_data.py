import random
import entities
import display
from economy_data import Transaction
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
        self.transaction = None
    

    def tick(self, game):
        if (self.transaction == None and 
            len(entities.shop['object'].transaction_queue) > 0 and 
            self.get_shop_tile() == 'cashier'
        ):
            game.action_log.append('transaction')
            game.pause()
            self.transact(entities.shop['object'].transaction_queue[0])
            game.unpause()
        if self.transaction != None:
            if self.get_shop_tile() != 'cashier': #If player moves from register,
                self.transaction = None           #transaction ends abruptly
                game.action_log.remove('transaction')
            else: # Transaction tick
                if self.transaction.stage == 0:
                    if game.keys[K_y]:
                        print "Transaction Stage set to 1!"
                        self.transaction.stage = 1


    def transact(self, hero):
        print "Transaction!"
        self.transaction = Transaction(self, hero)
         

    def get_shop_tile(self):
        return ref.shop_tile_dct[entities.shop['object'].shop_grid[
            self.location[1]/ref.tile_size][self.location[0]/ref.tile_size]
            ]['tile type']

