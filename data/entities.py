import pickle



def initialize():
    global player, weapons, heroes, adventure_sites, resource_sites, world, town
    import player_data
    player = player_data.get_new_player()
    weapons = {}
    heroes = {}
    adventure_sites = {}
    resource_sites = {}
    world = {}
    town = {}
    return


def load(save_name):
    global player, weapons, heroes, adventure_sites, resource_sites, world, town
    save_file = open('saves/%s' % save_name)
    dict_list = pickle.load(save_file)
    player = dict_list[0]
    weapons = dict_list[1]
    heroes = dict_list[2]
    adventure_sites = dict_list[3]
    resource_sites = dict_list[4]
    world = dict_list[5]
    town = dict_list[6]
    save_file.close()
    return


def save(save_name):
    global player, weapons, heroes, adventure_sites, resource_sites, world, town
    save_file = open('saves/%s' % save_name)
    dict_list = [player,
                 weapons, 
                 heroes, 
                 adventure_sites, 
                 resource_sites,
                 world,
                 town]
    pickle.dump(dict_list, save_file)
    save_file.close()
    return
    
