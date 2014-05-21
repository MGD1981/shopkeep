import pickle
import reference_data as ref
from random import randint

player = {}
weapons = {}
components = {}
heroes = {}
monsters = {}
sites = {}
world = {}
town = {}
shop = {}


def initialize():
    global player, weapons, components, heroes, monsters, sites, world, town, shop
    import world_data
    world = world_data.get_new_world(32)
    import site_data
    sites = {
        'next id': 1,
        'types': {},
        'object list': []
    }
    for site_type in ref.structure_type_dct.keys():
        sites['types'][site_type] = 0
    site_data.Site().generate('copper', 'rockland')
    for x in xrange(randint(ref.initial_range_of_sites[0], ref.initial_range_of_sites[1])):
        site_data.Site().generate('resource')
    import town_data
    town = {
        'object': town_data.Town().generate()
    }
    import player_data
    player = {
        'object': player_data.Player()
    }
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
    monsters = {
        'next id': 1,
        'object list': []
    }
    import shop_data
    shop = {
        'object': shop_data.Shop().generate('player')
    }

    return


def load(save_name):
    global player, weapons, components, heroes, monsters, sites, world, town, shop
    save_file = open('saves/%s' % save_name)
    dict_list = pickle.load(save_file)
    player = dict_list[0]
    weapons = dict_list[1]
    components = dict_list[2]
    heroes = dict_list[3]
    monsters = dict_list[4]
    sites = dict_list[5]
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
                 monsters,
                 sites, 
                 world,
                 town,
                 shop]
    pickle.dump(dict_list, save_file)
    save_file.close()
    return
    
