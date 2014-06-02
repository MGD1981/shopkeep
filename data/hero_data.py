import entities
import reference_data as ref
import copy
from shop_data import Shop
from economy_data import Economy
from random import choice, randint, shuffle
from math import copysign
from pathfinder import PathFinder
from gridmap import GridMap


class Hero():
    """Class holding unique hero object"""

    def __init__(self):
        self.hero_id = None 
        self.alive = True
        self.location = [None, None]
        self.shop_location = None
        self.shop_destination = None
        self.pathfinder = None
        self.path = None
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
        self.goals = []
        self.needs = []
        self.wants = []
        self.personality = None
        self.experience = None
        self.perceptions = None
        self.boredom = 0
        self.traveling = False
        self.destination = [None, None]
        self.coins = {
            'copper': 0,
            'silver': 0,
            'gold': 0
        }


    def tick(self, game):
        self.think()


        if self.location == entities.town['object'].location:
            if 'shopping' in self.wants:
                self.enter_shop(game)
                self.wants.remove('shopping')
            if self.shop_location == None:
                if randint(1, 5) == 1:
                    self.boredom += randint(1, 50)
                if self.boredom >= 100 and 'adventure' not in self.wants:
                #if self.boredom >= 1 and 'adventure' not in self.wants: #TODO: Remove line; just for testing
                    self.wants.append('adventure')
            else:
                pass

        if self.traveling:
            self.step_to(self.destination)
            if self.location == self.destination:
                self.traveling = False
                for site in entities.sites['object list']:
                    if self.destination == site.location:
                        site.structure.add_hero(self.hero_id)
                        self.destination = None
                        break
                    
        if 'adventure' in self.wants:
            shuffle(entities.sites['object list'])
            for site in entities.sites['object list']:
                if (ref.structure_type_dct[
                    site.structure.structure_type]['site type'] == 'adventure' and
                    site.structure.worker_capacity > 0
                ):
                    self.traveling = True
                    self.wants.remove('adventure')
                    self.boredom = 0
                    self.destination = site.location
                    break

    def think(self):
        if self.shop_location == None and len(self.inventory) >= 2 and 'shopping' not in self.wants:
            self.wants.append('shopping')
        if self.shop_location != None: #if hero is in the shop
            if self.inventory >= 2 and self.pathfinder == None:
                transaction_tiles = self.get_tiles('transaction')
                self.shop_destination = choice(transaction_tiles)
                self.get_path(self.shop_destination)

    def get_path(self, destination):
        gridmap = GridMap(
            len(entities.shop['object'].shop_grid[0]),
            len(entities.shop['object'].shop_grid)
        )
        blocked_tiles = self.get_tiles('passable', False)
        for blocked_tile in blocked_tiles:
            gridmap.set_blocked(blocked_tile)
        self.pathfinder = PathFinder(gridmap.successors, gridmap.move_cost, gridmap.move_cost)
        self.path = self.pathfinder.compute_path(
            tuple(map(lambda x: x/ref.tile_size, self.shop_location)),
            destination
        )


    def step_to(self, destination=None):
        x = False
        y = False
        if destination[0] != self.location[0]:
            x = True
        if destination[1] != self.location[1]:
            y = True
        if x and randint(1,3) != 3:
            self.location[0] = self.location[0] - int(
                copysign(1, self.location[0]-destination[0])
            )
        if y and randint(1,3) != 3:
            self.location[1] = self.location[1] - int(
                copysign(1, self.location[1]-destination[1])
            )


    def get_tiles(self, tile_type, positive=True):
        """Returns a list of coordinates where that type of tile exists in the shop grid"""
        if tile_type not in ref.tile_type_list:
            tester = tile_type
            tile_type = positive
        else:
            tester = 'tile type'
        tiles = []
        for row in xrange(len(entities.shop['object'].shop_grid)):
            for column in xrange(len(entities.shop['object'].shop_grid[row])):
                tile = entities.shop['object'].shop_grid[row][column]
                if tile in ref.shop_tile_dct.keys():
                    if ref.shop_tile_dct[tile][tester] == tile_type:
                        tiles.append((column, row))
        return tiles


        
    def enter_shop(self, game):
        shop_grid = entities.shop['object'].shop_grid
        door_locs = []
        for y in xrange(len(shop_grid)):
            for x in xrange(len(shop_grid[0])):
                if shop_grid[y][x] != 0:
                    if ref.shop_tile_dct[shop_grid[y][x]]['tile type'] == 'door':
                        door_locs.append((x, y))
        entrance_loc = choice(door_locs)
        self.shop_location = [
            entrance_loc[0] * ref.tile_size,
            entrance_loc[1] * ref.tile_size
        ]
        game.message_log += "%s has entered your shop." % self.name
        game.screens['world'].initialize_shop_sprites(game)


    def generate(self, location='random', weapon='random'):
        """Generates a hero."""
        import item_data
        import language
        self.personality = Personality()
        self.coins['copper'] = randint(10,300)
        if location == 'town':
            self.location = copy.deepcopy(entities.town['object'].location)
        if weapon != None:
            if weapon == 'random':
                self.inventory.append(item_data.Weapon().generate('random'))
            else:
                return NotImplementedError(weapon) #TODO
        self.name = language.create_name('human')
        if type(self.location) == list:
            entities.town['object'].population += 1
            entities.town['object'].occupations['adventurer'] += 1
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
                                             #Will be based on economy object of whatever town hero is from.
		self.world_perception = Personality() #Personality class object
		self.shopkeep_perception = Personality() #Personality class object
		self.shop_perception = Shop() #TODO: Shop class object
	

