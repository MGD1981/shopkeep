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
        self.monsters = []
        self.harvestable = {}
        

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
                #resources measured in grams
                self.harvestable['resources'] = [
                        choice(resource_possibilities),
                        randint(100, 1500)
                        ] #NOTE: These numbers suitable for metal, may not be for other materials
                          #NOTE: Mine production should be ~1kg pure metal per day per miner.
                          #NOTE: Real mine has ~43500kg before producing much less.
                            
        self.set_site_id()
        return self


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
        return self
                        
    def add_worker(self):
        self.workers += 1
        self.worker_capacity -= 1
                    
    def transform(self):
        if 'transformations' in ref.structure_type_dct[self.structure_type].keys():
            self.structure_type = choice(ref.structure_type_dct[self.structure_type]['transformations'])
            return self
        

