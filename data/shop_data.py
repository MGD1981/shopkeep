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
        self.surface = None #pygame surface for shop map
        self.background_tiles = None #group of sprites
        self.overlay = None #group of sprites


    def generate(self, arg):
        """Generates a new shop object."""
        if arg == 'player':
            self.shop_grid = ref.initial_shop_overlay
            self.surface = pg.Surface((
                    len(self.shop_grid)*ref.tile_size,
                    len(self.shop_grid[0])*ref.tile_size))
        return self


