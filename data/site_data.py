import entities
from random import randint


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
            terrain_type = entities.world['grid'][x][y]
            while terrain_type != 0:
                x = randint(0, size-1), y = randint(0, size-1)
            self.location = [x,y]
            self.structure = (Structure().generate('terrain_type'))

            if site_type = 'random':
                if randint(1,3) == 1:
                    self.site_type = 'adventure'
                else:
                    self.site_type = 'resource'
        self.set_site_id()
        return self


    def set_site_id(self):
        """Gives site object uniquue ID."""
        self.site_id = entities.sites['next id']
        entities.sites['object list'].append(self)
        entities.sites['next id'] += 1
        
    def __repr__(self):
        return 'Site(ID: %r, Type:%r, Loc: %r)' % (self.hero_id, self.site_type, self.location)
        

#TODO: Add structures to reference dict
class Structure():
    """Structure object which lives on sites."""
    
    def __init__(self):
        self.structure_type = None
        
    def generate(self, terrain_type):
        pass