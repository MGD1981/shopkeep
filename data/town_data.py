import reference_data as ref

def get_new_town():
    town = {
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
    for material_class in ref.material_class_dct.keys():
        town['resource'][material_class] = {}
        for material_type in ref.material_class_dct[material_class]:
            town['resource'][material_class][material_type] = {
                'harvestable': 0,
                'available': 0
            }

    return world