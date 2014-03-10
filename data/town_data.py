import reference_data as ref

def get_new_town():
    town = {
        'resource': {}
    }
    for material_class in ref.material_class_dct.keys():
        town['resource'][material_class] = {}
        for material_type in ref.material_class_dct[material_class]:
            town['resource'][material_class][material_type] = {
                'intrinsic value': 0,
                'harvestable': 0,
                'available': 0
            }

    return world