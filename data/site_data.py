import entities
import reference_data as ref
from random import randint, choice


class Site():
    """Site object which exists on the world map"""

    def __init__(self):
        self.site_id = None
        self.location = [None, None]
        self.structure = None
        self.resource = None
        self.harvestable = None
        

    def generate(self, site_type='random', arg='random'):
        """Generates a site based on type"""
        size = entities.world['size']
        if site_type == 'random':
            if randint(1,3) == 1:
                site_type = 'adventure'
            else:
                site_type = 'resource'
        elif site_type in ref.material_type_dct.keys():
            self.resource = site_type
            site_type = 'resource'
        terrain_list = None
        if arg == 'random':
            terrain_list = [x for x in ref.terrain_dct.keys() if type(x) == int]
        elif arg in ref.terrain_type_list:
            terrain_list = [
                x for x in ref.terrain_dct.keys() if ref.terrain_dct[x]['terrain type'] == arg
            ]
        x = randint(0, size-1)
        y = randint(0, size-1)
        terrain_type = entities.world['grid'][y][x]
        site_locations = [s.location for s in entities.sites['object list']]
        while terrain_type not in terrain_list or [x,y] in site_locations:
            x = randint(0, size-1)
            y = randint(0, size-1)
            terrain_type = entities.world['grid'][y][x]

        self.location = [x,y]
        self.structure = Structure().generate(
            ref.terrain_dct[terrain_type]['terrain type'], site_type
        )
        if self.resource == None:
            if 'resource type' in ref.structure_type_dct[
                self.structure.structure_type
                ].keys():
                resource_type = ref.structure_type_dct[
                    self.structure.structure_type]['resource type'
                ]
                resource_possibilities = []
                for possible_material in [
                    x for x in ref.material_class_dct[resource_type][
                    'types'] if 'rarity' in ref.material_type_dct[x].keys()
                ]:
                    for x in xrange(ref.rarity_dct[
                        ref.material_type_dct[possible_material]['rarity']
                    ]):
                        resource_possibilities.append(possible_material)
                self.resource = choice(resource_possibilities)
            #resources measured in grams
        if self.resource != None:
            self.harvestable = randint(100000, 1500000)
            try:
                entities.town['object'].resources[
                    ref.material_type_dct[self.resource]['class']][
                    self.resource]['harvestable'] += self.harvestable
            except KeyError:
                pass
            #NOTE: These numbers suitable for metal, may not be for other materials
            #NOTE: Mine production should be ~1kg pure metal per day per miner.
            #NOTE: IRL mine has ~43500kg before producing much less.
                        
        self.set_site_id()
        return self
    
    
    def tick(self, game, ticks=1):
        """Causes time to pass at site"""
        
        self.structure.time_until_harvest -= ticks
        if self.structure.time_until_harvest <= 0:
            if ref.structure_type_dct[self.structure.structure_type]['site type'] == 'resource':
                resources_harvested = 0
                for worker in xrange(self.structure.workers):
                    workload = randint(500, 1500)
                    if workload <= self.harvestable:
                        self.harvestable -= workload
                        resources_harvested += workload
                    else:
                        resources_harvested += self.harvestable
                        self.harvestable = 0
                        self.structure.workers = 0
                        self.structure.transform()
                        game.action_log.append('transformation')
                        break
                #Adds resource to 'available' town resources
                entities.town['object'].resources[
                    ref.material_type_dct[self.resource]['class']][
                    self.resource]['available'] += resources_harvested
                #Removes resource from 'harvestable' town resources
                entities.town['object'].resources[
                    ref.material_type_dct[self.resource]['class']][
                    self.resource]['harvestable'] -= resources_harvested

                self.structure.time_until_harvest = ref.structure_type_dct[
                        self.structure.structure_type]['time per harvest']
                return

            elif ref.structure_type_dct[self.structure.structure_type]['site type'] == 'adventure':
                if len(self.structure.workers) > 0:
                    for hero in [h for h in entities.heroes['object list'] if (
                            h.hero_id in self.structure.workers)]:
                        hero.boredom += randint(0, 100)
                        try:
                            monster = next(m for m in entities.monsters['object list'] if 
                                           m.monster_id in self.structure.monsters)
                            self.battle(hero, monster)
                        except StopIteration:
                            adventure_sites = [
                                s for s in entities.sites['object list'] if ref.structure_type_dct[
                                s.structure.structure_type]['site type'] == 'adventure'
                            ]
                            if hero.boredom < 100 and len(adventure_sites) > 0:
                                hero.destination = choice(adventure_sites).location
                            else:
                                hero.boredom = 0
                                hero.destination = entities.town['object'].location
                            hero.traveling = True
                            self.structure.workers.remove(hero.hero_id)
                            self.structure.worker_capacity += 1
                            
                        
                        
    def battle(self, hero, monster):
        """Hero and monster fight."""
        #TODO: Will add more when monsters get fleshed out.
        victor = choice([hero, monster])
        if victor == hero:
            loser = monster
            entities.monsters['object list'].remove(loser)
            self.structure.monsters.remove(loser.monster_id)
        else:
            loser = hero
            entities.heroes['object list'].remove(loser)
            self.structure.workers.remove(loser.hero_id)
            self.structure.worker_capacity += 1
        victor.kills.append(loser)
        loser.alive = False
        for coin in loser.coins.keys():
            victor.coins[coin] += loser.coins[coin]
        for item in loser.inventory:
            victor.inventory.append(item)




    def set_site_id(self):
        """Gives site object unique ID."""
        self.site_id = entities.sites['next id']
        entities.sites['object list'].append(self)
        entities.sites['next id'] += 1
        
    def __repr__(self):
        return 'Site(ID: %r, Type:%r, Loc: %r)' % (
                self.site_id, self.structure.structure_type, self.location)
        

class Structure():
    """Structure object which lives on sites."""
    
    def __init__(self):
        self.structure_type = None
        self.worker_capacity = None
        self.workers = None
        self.monsters = None
        self.time_until_harvest = None
        
        
    def generate(self, terrain_type='random', site_type='random'):
        """Generates a structure at a site"""
        if terrain_type == 'random' and site_type == 'random':
            self.structure_type = choice(ref.structure_type_dct.keys())
        elif site_type == 'random':
            self.structure_type = choice(ref.structure_class_dct[terrain_type])
        elif terrain_type == 'random':
            self.structure_type = choice(ref.site_type_dct[site_type])
        else:
            self.structure_type = choice(
                [x for x in ref.site_type_dct[site_type] if ref.structure_type_dct[
                x]['class'] == terrain_type]
            )
        if self.get_attribute('site type') == 'resource':
            self.workers = 0
        else:
            self.workers = []
            self.monsters = []
        self.worker_capacity = self.get_attribute('worker capacity')
        self.time_until_harvest = self.get_attribute('time per harvest')
        return self

    def get_attribute(self, attribute):
        try:
            return ref.structure_type_dct[self.structure_type][attribute]
        except KeyError:
            return KeyError("Invalid attribute of structure: %r" % attribute)
                       
    def add_worker(self):
        self.workers += 1
        self.worker_capacity -= 1
        
    def add_hero(self, hero_id):
        self.workers.append(hero_id)
        self.worker_capacity -= 1

    def add_monster(self, monster_id):
        self.monsters.append(monster_id)

    def transform(self):
        if 'transformations' in ref.structure_type_dct[self.structure_type].keys():
            self.structure_type = choice(self.get_attribute('transformations'))
            if self.get_attribute('site type') == 'resource':
                self.workers = 0
            else:
                self.workers = []
                self.monsters = []

