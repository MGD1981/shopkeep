import entities
from random import choice


class Shop():
	"""Shop class object"""
	
	def __init__(self):
		self.player_owned = False
		self.shop_grid = None
		self.security = None
		self.decor = None
		
	def generate(self, arg):
		"""Generates a new shop object."""
		if arg == 'player':
			self.shop_grid = []
			
		return self