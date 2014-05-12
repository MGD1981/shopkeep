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


    def generate(self, arg):
        """Generates a new shop object."""
        if arg == 'player':
            self.shop_grid = ref.initial_shop_overlay
        return self


