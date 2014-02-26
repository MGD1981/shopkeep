import pickle


def initialize():
    global weapons, heroes, adventure_sites, resource_sites
    weapons = {}
    heroes = {}
    adventure_sites = {}
    resource_sites = {}
    return


def load(save_name):
    global weapons, heroes, adventure_sites, resource_sites
    save_file = open('saves/%s' % save_name)
    dict_list = pickle.load(save_file)
    weapons = dict_list[0]
    heroes = dict_list[1]
    adventure_sites = dict_list[2]
    resource_sites = dict_list[3]
    save_file.close()
    return


def save(save_name):
    global weapons, heroes, adventure_sites, resource_sites
    save_file = open('saves/%s' % save_name)
    dict_list = [weapons, 
                 heroes, 
                 adventure_sites, 
                 resource_sites]
    pickle.dump(dict_list, save_file)
    save_file.close()
    return
    
