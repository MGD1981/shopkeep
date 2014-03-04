import entities
import weapon_data


class Economy():
	"""Economy class object."""
	
	def __init__():
		weapon_value_table = {}
		material_value_table = {}
		
		#A specific weapon has its value stored by adding its weapon_id key
		for weapon_type in weapon_data.Weapon.weapon_type_dct:
			weapon_value_table[weapon_type] = None #initializes each weapon_type price as None
		for material_class in weapon_data.Material.material_class_dct:
			for material_type in material_class['type']:
				material_value_table[material_type] = None #initializes each material_type price as None

			