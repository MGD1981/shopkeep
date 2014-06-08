import reference_data as ref
from economy_data import Economy
from entities import world, sites
import site_data
from random import randint, choice, shuffle

class Town():

    def __init__(self):
        self.location = [None, None]
        self.resources = {}
        self.population = 1
        self.occupations = {
            'adventurer': 0,
            'farmer': 0,
            'miner': 0,
            'woodcutter': 0,
            'artisan': 0,
            'homekeeper': 0,
            'government': 0,
            'retail': 1
        }
        self.standard_currency = 'copper'
        self.economy = None


    def generate(self):
        #Set location
        self.economy = Economy().generate(self)
        w_size = world['size']
        self.location[0] = randint(w_size - (3*w_size/4), w_size - (w_size/4))
        self.location[1] = randint(w_size - (3*w_size/4), w_size - (w_size/4))
        world['grid'][self.location[1]][self.location[0]] = 't'

        #Populate resources
        for material_class in ref.material_class_dct.keys():
            self.resources[material_class] = {}
            for material_type in ref.material_class_dct[material_class]['types']:
                self.resources[material_class][material_type] = {
                    'harvestable': 0,
                    'available': 0
                }
        for site in sites['object list']:
            if ref.structure_type_dct[site.structure.structure_type]['site type'] == 'resource':
                self.resources[ref.material_type_dct[
                    site.resource]['class']][site.resource]['harvestable'] += site.harvestable

        return self.populate_town()
    
    
    def populate_town(self, people=50):
        """Populates a town with people, each with an occupation."""
        
        #1.5 acres farm needed per person
        #farmer could farm 20-40 (30) acres
        #30/1.5 = 20 people per farm
        people_to_assign = people
        farms_needed = (self.population + people)/20 + 1
        if people_to_assign >= farms_needed:
            self.occupations['farmer'] += farms_needed
            people_to_assign -= farms_needed
        else:
            self.occupations['farmer'] += people_to_assign
        shuffle(sites['object list'])
        while people_to_assign > 0:
            for site in [
                x for x in sites['object list'] if ref.structure_type_dct[x.structure.structure_type]['site type'] == 'resource'
            ]:
                if site.structure.worker_capacity > 0:
                    self.occupations[ref.structure_type_dct[
                        site.structure.structure_type]['worker type']] += 1
                    site.structure.add_worker()
                    people_to_assign -= 1
                    continue
            self.occupations[choice(
                    ['artisan']*2 + 
                    ['homekeeper']*5 + 
                    ['government'] +
                    ['retail']*2)] += 1
            people_to_assign -= 1            
        
        self.population += people
        return self


    def tick(self, game):
        pass
