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
        self.resources = {}

    def generate(self, arg):
        """Generates a new shop object."""
        if arg == 'player':
            self.shop_grid = ref.initial_shop_overlay
        for material_class in ref.material_class_dct.keys():
            self.resources[material_class] = {}
            for material_type in ref.material_class_dct[material_class]['types']:
                self.resources[material_class][material_type] = 0
        return self


