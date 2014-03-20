import entities
import reference_data as ref
from random import randint, choice


class Site()
    """Site object which exists on the world map"""

    def __init__(self):
        self.site_id = None
        self.site_type = None
        self.location = [None, None]
        self.structure = None
        self.monsters = [] #list of monster ids
        self.resource = None
        self.harvestable = None
        

    def generate(self, site_type='random', arg='random'):
        """Generates a site based on type"""
        size = entities.world['size']
        if arg == 'random':
            x = randint(0, size-1), y = randint(0, size-1)
            terrain_type = ref.terrain_dct[entities.world['grid'][x][y]]
            while terrain_type not in [0, 't']:
                x = randint(0, size-1), y = randint(0, size-1)
            self.location = [x,y]
            if site_type = 'random':
                if randint(1,3) == 1:
                    self.site_type = 'adventure'
                else:
                    self.site_type = 'resource'
            else:
                self.site_type = site_type
                
            self.structure = Structure().generate(ref.terrain_dct[terrain_type], self.site_type)
            if 'resource type' in ref.structure_type_dct[self.structure.structure_type].keys():
                resource_type = ref.structure_type_dct[self.structure.structure_type]['resource type']
                resource_possibilities = []
                for possible_material in ref.material_class_dct[resource_type]:
                    for x in xrange(ref.rarity_dct[ref.material_type_dct[possible_material]['rarity']]):
                        resource_possibilities.append possible_material
                self.resource = choice(resource_possibilities)
                #resources measured in grams
                self.harvestable = randint(100000, 1500000)
                #NOTE: These numbers suitable for metal, may not be for other materials
                #NOTE: Mine production should be ~1kg pure metal per day per miner.
                #NOTE: IRL mine has ~43500kg before producing much less.
                            
        self.set_site_id()
        return self
        
        
    def tick(self, seconds=1):
        """Causes time to pass at site"""
        self.structure.time_until_harvest -= seconds
        if self.structure.time_until_harvest <= 0:
            resources_harvested = 0
            for worker in self.structure.workers:
                workload = randint(500, 1500)
                if workload <= self.harvestable:
                    self.harvestable -= workload
                    resources_harvested += workload
                else:
                    resources_harvested += self.harvestable
                    self.harvestable = 0
                    self.structure.workers = 0
                    self.structure.transform()
                    entities.town['resource'][self.resource] += resources_harvested
                    return
            entities.town['resource'][self.resource] += resources_harvested
            self.structure.time_until_harvest = 60 #TODO: Get from ref


    def set_site_id(self):
        """Gives site object uniquue ID."""
        self.site_id = entities.sites['next id']
        entities.sites['object list'].append(self)
        entities.sites['next id'] += 1
        
    def __repr__(self):
        return 'Site(ID: %r, Type:%r, Loc: %r)' % (
                self.hero_id, self.site_type, self.location)
        

class Structure():
    """Structure object which lives on sites."""
    
    def __init__(self):
        self.structure_type = None
        self.worker_capacity = None
        self.workers = None
        self.time_until_harvest = None
        
        
    def generate(self, terrain_type='random', site_type='random'):
        """Generates a structure at a site"""
        if terrain_type == 'random' and site_type == 'random':
            self.structure_type = choice(ref.structure_type_dct.keys())
        elif site_type == 'random':
            self.structure_type = choice(ref.structure_class_dct[terrain_type])
        elif terrain_type == 'random':
            self.structure_type = choice(ref.site_type_dct[site_type])
        self.workers = 0
        self.worker_capacity = ref.structure_type_dct[self.structure_type]['worker capacity']
        self.time_until_harvest = 60 #TODO: Add specific 'time per harvest' in ref for each resource type
                                     #This will eliminate need to add different workload amounts for each
        return self
                        
    def add_worker(self):
        self.workers += 1
        self.worker_capacity -= 1
                    
    def transform(self):
        if 'transformations' in ref.structure_type_dct[self.structure_type].keys():
            self.structure_type = choice(ref.structure_type_dct[self.structure_type]['transformations'])
            return self
        

