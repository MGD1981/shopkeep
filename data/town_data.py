import reference_data as ref
from entities import world, sites
from random import randint, choice, shuffle

def get_new_town():
    town = {
        'location': [None, None],
        'resource': {},
        'population': 1,
        'occupation': {
            'adventurer': 0,
            'farmer': 0,
            'miner': 0,
            'woodcutter': 0,
            'artisan': 0,
            'homekeeper': 0,
            'government': 0,
            'retail': 1
        }
    }

    #Set location
    w_size = world['size']
    town['location'][0] = randint(w_size - (3*w_size/4), w_size - (w_size/4))
    town['location'][1] = randint(w_size - (3*w_size/4), w_size - (w_size/4))
    world['grid'][town['location'][0]][town['location'][1]] = 't'

    #Populate resources
    for material_class in ref.material_class_dct.keys():
        town['resource'][material_class] = {}
        for material_type in ref.material_class_dct[material_class]['types']:
            town['resource'][material_class][material_type] = {
                'harvestable': 0,
                'available': 0
            }

    return populate_town(town)
    
    
def populate_town(town, people=50):
    """Populates a town with people, each with an occupation."""
    
    #1.5 acres farm needed per person
    #farmer could farm 20-40 (30) acres
    #30/1.5 = 20 people per farm
    people_to_assign = people
    farms_needed = (town['population'] + people)/20 + 1
    if people_to_assign >= farms_needed:
        town['occupation']['farmer'] += farms_needed
        people_to_assign -= farms_needed
    else:
        town['occupation']['farmer'] += people_to_assign
    shuffle(sites)
    while people_to_assign > 0:
        for site in sites:
            if site.structure.worker_capacity > 0:
                town['occupation'][ref.structure_type_dct[site.structure]['worker type']] += 1
                site.structure.add_worker()
                people_to_assign -= 1
                continue
        town['occupation'][choice(
                ['artisan']*2 + 
                ['homekeeper']*5 + 
                ['government'] +
                ['retail']*2)] += 1
        people_to_assign -= 1            
    
    town['population'] += people
    return town
