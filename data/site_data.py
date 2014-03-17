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
            if 'resource type' in ref.structure_type_dct[Structure.structure_type].keys():
                self.harvestable['resources'] = []
                self.harvestable['resources'].append([
                        ref.structure_type_dct[Structure.structure_type]['resource type'],
                        randint(50, 500)]) #TODO: Get good numbers for possible resource amounts
                            
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
        
    def generate(self, terrain_type='random', site_type='random'):

        if terrain_type == 'random' and site_type == 'random':
            self.structure_type = choice(ref.structure_type_dct.keys())
        elif site_type == 'random':
            self.structure_type = choice(ref.structure_class_dct[terrain_type])
        elif terrain_type == 'random':
            self.structure_type = choice(ref.site_type_dct[site_type])
            return self
            
    def transform(self):
        if 'transformations' in ref.structure_type_dct[self.structure_type].keys():
            self.structure_type = choice(ref.structure_type_dct[self.structure_type]['transformations'])
            return self
        

