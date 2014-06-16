import entities
import reference_data as ref
import item_data


class Economy():
    """Economy class object."""

    def __init__(self):
        #Values are per kg
        self.weapon_value_table = {}
        self.material_value_table = {}
        self.coin_standard = None #coins are 10g of material

        #A specific weapon has its value stored by adding its weapon_id key NOTE: Maybe not -- what was I thinking?
        for weapon_type in ref.weapon_type_dct:
            self.weapon_value_table[weapon_type] = None #initializes each weapon_type price as None
        for material_type in ref.material_class_dct.keys():
            self.material_value_table[material_type] = None #initializes each material_type price as None

    def generate(self, town=None, coin_standard=None):
        """Generates values for a town's Economy object."""
        if town == None:
            town = entities.town['object']
        if coin_standard == None:
            coin_standard = town.standard_currency
        self.material_value_table[coin_standard] = 100
        useable_materials = []
        non_useable_materials = []
        for resource_class in town.resources.keys(): #for each material class...
            for material in town.resources[resource_class]: #for each material in that class...
                if ref.material_type_dct[material]['useable']: #if material has traits:
                    useable_materials.append(material)
                else:
                    non_useable_materials.append(material)
        for material in useable_materials:
            resource_class = ref.material_type_dct[material]['class']
            m_available = town.resources[resource_class][material]['available']
            m_harvestable = town.resources[resource_class][material]['harvestable']                
            if m_available + m_harvestable == 0:
                self.material_value_table[material] = None
                continue
            m_toughness = (
                ref.material_type_dct[material]['toughness'] *
                ref.material_class_dct[resource_class]['trait factor']['toughness']
            )
            m_strength = (
                ref.material_type_dct[material]['strength'] * 
                ref.material_class_dct[resource_class]['trait factor']['strength']
            )
            m_flexibility = (
                ref.material_type_dct[material]['flexibility'] * 
                ref.material_class_dct[resource_class]['trait factor']['flexibility']
            )
            supply = (m_available + (m_harvestable*0.15))
            _demand = 0.0
            for occupation in town.occupations.keys():
                people = town.occupations[occupation]
                _demand += (
                    ref.occupation_type_dct[occupation][
                    'material requirements']['toughness'] * m_toughness
                )
                _demand += (
                    ref.occupation_type_dct[occupation][
                    'material requirements']['strength'] * m_strength
                )
                _demand += (
                    ref.occupation_type_dct[occupation][
                    'material requirements']['flexibility'] * m_flexibility
                )
                _demand = _demand * people
            demand = _demand * 1000
            self.material_value_table[material] = demand/supply
            
        for material in non_useable_materials:
            resource_class = ref.material_type_dct[material]['class']
            m_available = town.resources[resource_class][material]['available']
            m_harvestable = town.resources[resource_class][material]['harvestable']
            if m_available + m_harvestable == 0:
                self.material_value_table[material] = None
                continue
            base_value = self.material_value_table[
                ref.material_type_dct[material]['material yielded']]
            if base_value == None:
                base_value = 1
            supply = (m_available + (m_harvestable*0.15))
            self.material_value_table[material] = (
                base_value * (float(town.population)/supply*1000)
            )

        return self
		
	
	def convert_value_tables(self, new_coin_standard):
		"""Converts all values in the value tables to the passed-in denomination."""
		pass
		
	
    def get_value(self, item, coin_standard=None):
        """Returns value of item in passed-in denomination based on current Economy object"""
        if coin_standard == None:
            coin_standard = entities.town['object'].standard_currency

        if type(item) == item_data.Component:
	        pass	

		
	def be_influenced(self, economy_x):
		"""Adjusts (weighted) table values in conjunction with another Economy class."""
		pass


class Transaction():

    def __init__(self, player, hero):
        self.player = player
        self.hero = hero

        self.player_offer = []
        self.hero_offer = []

    def get_display_text(self):
        """Returns a list of strings to display on the message screen."""
        text_list = []
        text_list.extend([
            "Transaction!",
            "Hero: %s" % self.hero.name,
            "Inventory: %s" % str(self.hero.inventory)
        ])
        return text_list
