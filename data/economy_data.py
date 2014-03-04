import entities
import weapon_data


class Economy():
	"""Economy class object."""
	
	def __init__():
		for weapon_type in weapon_data.Weapon.weapon_type_dct:
			exec("self.%s = None" % weapon_type) #initializes each weapon_type price as None
		for material_class in weapon_data.Material.material_class_dct:
			for material_type in material_class['type']:
				exec("self.%s = None" % material_type) #initializes each material_type price as None

			