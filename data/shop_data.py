import entities
import reference_data as ref
from random import choice
import display


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


    def tick(self, game):
        """Tick function for Shop object"""
        display.draw_screen.draw_shop_background(game,
                                     len(self.shop_grid),
                                     len(self.shop_grid[0]),
                                     ref.image_path + ref.shop_tile_dct[1]['image file'])
        return 

