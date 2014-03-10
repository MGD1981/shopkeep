import pickle

player = {}
weapons = {}
components = {}
heroes = {}
adventure_sites = {}
resource_sites = {}
world = {}
town = {}
shop = {}


def initialize():
    global player, weapons, components, heroes, adventure_sites, resource_sites, world, town
    import player_data
    import world_data
    world = world_data.get_new_world()
    player = player_data.get_new_player()
    weapons = {
        'next id': 1,
        'object list': []
    }
    components = {
        'next id': 1,
        'object list': []
    }
    heroes = {
        'next id': 1,
        'object list': []
    }
    adventure_sites = {
        'next id': 1,
        'object list': []
    }
    resource_sites = {
        'next id': 1,
        'object list': []
    }
    town = {}
    shop = {}
    return


def load(save_name):
    global player, weapons, components, heroes, adventure_sites, resource_sites, world, town, shop
    save_file = open('saves/%s' % save_name)
    dict_list = pickle.load(save_file)
    player = dict_list[0]
    weapons = dict_list[1]
    components = dict_list[2]
    heroes = dict_list[3]
    adventure_sites = dict_list[4]
    resource_sites = dict_list[5]
    world = dict_list[6]
    town = dict_list[7]
    shop = dict_list[8]
    save_file.close()
    return


def save(save_name):
    global player, weapons, components, heroes, adventure_sites, resource_sites, world, town, shop
    save_file = open('saves/%s' % save_name)
    dict_list = [player,
                 weapons,
                 components,
                 heroes, 
                 adventure_sites, 
                 resource_sites,
                 world,
                 town,
                 shop]
    pickle.dump(dict_list, save_file)
    save_file.close()
    return
    
