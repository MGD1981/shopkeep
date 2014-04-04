import entities
import reference_data as ref
from random import choice
import display
import pygame as pg


class Shop():
    """Shop class object"""
	
    def __init__(self):
        self.player_owned = False
        self.security = None
        self.decor = None
        self.shop_grid = None
        self.surface = None


    def generate(self, arg):
        """Generates a new shop object."""
        if arg == 'player':
            self.shop_grid = ref.initial_shop_overlay
            self.surface = pg.Surface((len(self.shop_grid)*32,len(self.shop_grid[0])*32))
        return self


    def tick(self, game):
        """Tick function for Shop object"""
        display.draw_screen.draw_shop_background(game,
                                     len(self.shop_grid),
                                     len(self.shop_grid[0]),
                                     ref.image_path + ref.shop_tile_dct[1]['image file'])
        return 

