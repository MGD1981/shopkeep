import entities
from shop_data import Shop
from economy_data import Economy
from random import choice


class Hero():
    """Class holding unique hero object"""

    def __init__(self):
        self.hero_id = None 
        self.location = [None, None]
        self.name = None
        self.home = None
        self.inventory = []
        self.coins = {
            'copper': 0,
            'silver': 0,
            'gold': 0
        }
        self.kills = []
        self.size = 100 #represents percent of "normal" size
        self.goals = None
        self.needs = None
        self.wants = None
        self.personality = None
        self.experience = None
        self.perceptions = None


    def generate(self, arg='random'):
        """Generates a hero."""
        import language
        if arg == 'random':
            self.coins['copper'] = randint(10,300)
        self.name = language.create_name('human')
        self.set_hero_id()
        return self


    def set_hero_id(self):
        """Gives hero object uniquue ID."""
        self.hero_id = entities.heroes['next id']
        entities.heroes['object list'].append(self)
        entities.heroes['next id'] += 1
		

    def __repr__(self):
        return 'Hero(ID: %r, Name:%r)' % (self.hero_id, self.name)


		
class Personality():
	"""Class holding quantitative personality traits (0 = neutral).
	   Personalities are able to be saved as templates.
	   Default initialization creates pure neutral personality."""

	def __init__(self):
		self.shrewdness = 0 #ability to assess truth (battle effective)
		self.guile = 0 #ability to lie (battle effective)
		self.honesty = 0 #tendency to tell truth
		self.charisma = 0 #likability
		self.patience = 0 #ability to remain calm when angered/annoyed (battle effective)
		self.fussiness = 0 #tendency to become angered/annoyed
		self.seriousness = 0 #tendency to take things seriously (battle effective)
		self.discipline = 0 #ability to control own base nature (battle effective)


class Experience():
	"""Class containing weapon and monster familiarities/knowledge"""
	
	def __init__(self):
		self.weapon_experience = None #table of weapon abilities and knowledge (class object?)
		self.monster_experience = None #table of monster familiarity (class object?)


class Perceptions():
	"""Class containing perceptions of world, economy, shop, and shopkeep"""

	def __init__(self):
		self.economic_perception = Economy() #TODO: Economy class object
		self.world_perception = Personality() #Personality class object
		self.shopkeep_perception = Personality() #Personality class object
		self.shop_perception = Shop() #TODO: Shop class object
	

