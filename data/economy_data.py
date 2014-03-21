import entities
import reference_data as ref


class Economy():
	"""Economy class object."""
	
	def __init__(self):
		#Values are per kg
		weapon_value_table = {}
		material_value_table = {}
		coin_standard = None #coins are 10g of material
		
		#A specific weapon has its value stored by adding its weapon_id key
		for weapon_type in ref.weapon_type_dct:
			weapon_value_table[weapon_type] = None #initializes each weapon_type price as None
		for material_class in ref.material_class_dct:
			for material_type in material_class['type']:
				material_value_table[material_type] = None #initializes each material_type price as None

	def generate(self, coin_standard='copper'):
		"""Generates values for the Economy object."""
		self.material_value_table[coin_standard] = 100
		
		return self
		
	
	def convert_value_tables(self, new_coin_standard):
		"""Converts all values in the value tables to the passed-in denomination."""
		pass
		
	
	def get_price(self, coin_standard=None):
		"""Returns the price of the value in the passed-in denomination."""
		if coin_standard == None:
			coin_standard = self.coin_standard
		pass
		
		
	def be_influenced(self, economy_x):
		"""Adjusts (weighted) table values in conjunction with another Economy class."""
		pass