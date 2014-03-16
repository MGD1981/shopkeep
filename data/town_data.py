import reference_data as ref
from entities import world
from random import randint

def get_new_town():
    town = {
        'location': [None, None],
        'resource': {},
        'occupation': {
            'adventurer': 0,
            'farmer': 0,
            'shepherd': 0,
            'hunter': 0,
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
        for material_type in ref.material_class_dct[material_class]:
            town['resource'][material_class][material_type] = {
                'harvestable': 0,
                'available': 0
            }

    return town

