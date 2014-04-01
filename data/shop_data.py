import entities
import reference_data as ref
from random import choice


class Shop():
	"""Shop class object"""
	
	def __init__(self):
		self.player_owned = False
		self.security = None
		self.decor = None
		
	def generate(self, arg):
		"""Generates a new shop object."""
		if arg == 'player':
			shop_grid = ref.initial_shop_overlay
			
		return {
                'shopmap': shop_grid,
                'object': self
               }
