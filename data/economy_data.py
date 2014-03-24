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

	def generate(self, town, coin_standard='copper'):
		"""Generates values for a town's Economy object."""
		self.material_value_table[coin_standard] = 100
        useable_materials = []
        non_useable_materials = []
        for resource_class in town['resource'].keys(): #for each material class...
            for material in resource_class['material']: #for each material in that class...
                if 'useable' in ref.material_type_dct[material].keys(): #if material has traits:
                    useable_materials.append(material)
                else:
                    non_useable_materials.append(material)
            for material in useable_materials
                m_available = town['resource'][resource_class][material]['available']
                m_harvestable = town['resource'][resource_class][material]['harvestable']                
                m_toughness = (ref.material_type_dct[material]['toughness'] *
                               ref.material_class_dct[resource_class]['trait factor']['toughness']) #TODO: Add this factor to material_class_dct)
                m_strength = (ref.material_type_dct[material]['strength'] * 
                              ref.material_class_dct[resource_class]['trait factor']['strength'])
                m_flexibility = (ref.material_type_dct[material]['flexibility'] * 
                                 ref.material_class_dct[resource_class]['trait factor']['flexibility'])
                supply = (m_available + (m_harvestable*0.15))
                _demand = 0.0
                for occupation in town['occupation'].keys():
                    people = town['occupation'][occupation]
                    _demand += (ref.occupation_type_dct[occupation]['material requirements']['toughness'] *
                               m_toughness)
                    _demand += (ref.occupation_type_dct[occupation]['material requirements']['strength'] *
                               m_strength)
                    _demand += (ref.occupation_type_dct[occupation]['material requirements']['flexibility'] *
                               m_flexibility)
                    _demand = _demand * people
                demand = _demand * 1000
                self.material_value_table[material_type] = demand/supply
                
            for material in non_useable_materials:
                m_available = town['resource'][resource_class][material]['available']
                m_harvestable = town['resource'][resource_class][material]['harvestable']
                base_value = self.material_value_table[ref.material_type_dct[material]['material yielded']] #TODO: Add to ref
                supply = (m_available + (m_harvestable*0.15))
                self.material_value_table[material_type] = base_value * (town['population']/supply*1000)
                
        
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