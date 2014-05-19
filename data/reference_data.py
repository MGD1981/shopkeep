from math import pi


screen = (1280, 1024)
#screen = (640, 512)

image_path = 'img/'

fps = 60

background_color = (39, 39, 39)
primary_color = (255, 255, 208)

initial_shop_overlay = [[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,2,2,2,2,2,2],
                        [0,0,0,0,2,4,1,1,1,2],
                        [0,0,0,0,2,1,1,5,5,2],
                        [0,0,0,0,2,1,1,1,1,2],
                        [0,0,0,0,2,1,1,1,1,2],
                        [0,0,0,0,2,2,2,3,2,2]]

tile_size = screen[0] / 20
scale = tile_size/32.0
initial_player_position = [7,5]
player_speed = 2

initial_range_of_sites = (1,3)

shop_tile_dct = {
    1: {
        'tile type': 'floor',
        'tile class': 'base',
        'passable': True,
        'image file': 'floor.png'
    },
    2: {
        'tile type': 'wall',
        'tile class': 'overlay',
        'passable': False,
        'image file': 'wall.png'
    },
    3: {
        'tile type': 'door',
        'tile class': 'overlay',
        'passable': True,
        'image file': 'floor.png'
    },
    4: {
        'tile type': 'stairs',
        'tile class': 'overlay',
        'passable': True,
        'image file': 'floor.png'
    },
    5: {
        'tile type': 'counter',
        'tile class': 'overlay',
        'passable': False,
        'image file': 'wall.png' 
    }
}


button_dct = {
    'shop': {
        'order': 0,
        'image file': 'shop_button.png'
    },
    'world': {
        'order': 1,
        'image file': 'world_button.png'
    },
    'town info': {
        'order': -1,
        'image file': 'town_info_button.png'
    },
    'world info': {
        'order': -2,
        'image file': 'world_info_button.png'
    }
}


sprite_dct = {
    'player': 'shopkeeper.png'
}

weapon_type_dct = {
    'spear': {
        'class': 'polearm',
        'components': ['shaft', 'head'],
        'hands to wield': 2
    },
    'dirk': {
        'class': 'dagger',
        'components': ['hilt', 'blade', 'scabbard'],
        'hands to wield': 1
    },
    'shortsword': {
        'class': 'sword',
        'components': ['hilt', 'blade', 'scabbard'],
        'hands to wield': 1
    },
    'longsword': {
        'class': 'sword',
        'components': ['hilt', 'blade', 'scabbard'],
        'hands to wield': 2
    },
    'flail': {
        'class': 'blunt',
        'components': ['handle', 'chain', 'ball'],
        'hands to wield': 1
    },
    'double flail': {
        'class': 'blunt',
        'components': ['handle', 'chain', 'ball', 'chain', 'ball'],
        'hands to wield': 1
    },
    'battle axe': {
        'class': 'cleave',
        'components': ['haft', 'blade'],
        'hands to wield': 2
    }
}


weapon_class_dct = {}
for weapon_type in weapon_type_dct.keys():
    weapon_class = weapon_type_dct[weapon_type]['class']
    if weapon_class not in weapon_class_dct.keys():
        weapon_class_dct[weapon_class] = []
    weapon_class_dct[weapon_class].append(weapon_type)
del weapon_type, weapon_class

#Volume in cm^3
component_type_dct = {
    'shaft': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': [('multi', 'point')],
        'volume': 200 * (pi * (1.25*1.25))
    },
    'head': {
        'class': 'point',
        'possible materials': ['stone', 'metal'],
        'joints': [('single', 'point')],
        'volume': 340
    },
    'hilt': {
        'class': 'base',
        'possible materials': ['wood', 'stone', 'metal'],
        'joints': [('single', 'edge')],
        'volume': 45
    },
    'blade': {
        'class': 'edge',
        'possible materials': ['metal'],
        'joints': [('single', 'base')],
        'volume': 180
    },
    'scabbard': {
        'class': 'standalone',
        'possible materials': ['leather', 'wood', 'metal'],
        'joints': [],
        'volume': 180
    },
    'haft': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': [('multi', 'edge')],
        'volume': 69 * (pi * (1.25*1.25))
    },
    'handle': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': [('multi', 'flagellum')],
        'volume': 150 * (pi * (1.25*1.25))
    },
    'chain': {
        'class': 'flagellum',
        'possible materials': ['metal'],
        'joints': [('single', 'base'), ('optional', 'finger')],
        'volume': 12 * (7.5 * (pi * (0.75*0.75)))
    },
    'ball': {
        'class': 'finger',
        'possible materials': ['metal'],
        'joints': [('single', 'flagellum')],
        'volume': (4/3)*pi*8*8*8
    },
    'limb': {
        'class': 'extension',
        'possible materials': ['wood'],
        'joints': [('single', 'base'), ('single', 'string')]
    },
    'bowstring': {
        'class': 'string',
        'possible materials': ['fiber'],
        'joints': [('single', 'extension'), ('single', 'extension')]
    }
}


component_class_dct = {}
for component_type in component_type_dct.keys():
    component_class = component_type_dct[component_type]['class']
    if component_class not in component_class_dct.keys():
        component_class_dct[component_class] = []
    component_class_dct[component_class].append(component_type)
del component_type, component_class


#Density measured in (g x cm)^3
#Toughness (Vickers [stone, metal], Crushing Strength [wood], Tensile Strength [fiber]) in MPa
#Strength (Young's modulus, Elastic modulus) in GPa
#Flexibility (Shear modulus, Modulus of rupture) in MPa, Elongation [fiber] in % as decimal
#Rarity (crustal abundance in ppm)
material_type_dct = {
    'bodark': {
        'class': 'wood',
        'toughness': 64.7,
        'strength': 11.64,
        'flexibility': 128.6,
        'rarity': 'common',
        'density': 0.855,
        'useable': True
    },
    'ipay': {
        'class': 'wood',
        'toughness': 93.8,
        'strength': 22.07,
        'flexibility': 177.0,
        'rarity': 'rare',
        'density': 1.100,
        'useable': True
    },
    'lemonwood': {
        'class': 'wood',
        'toughness': 67.5,
        'strength': 15.75,
        'flexibility': 152.4,
        'rarity': 'very rare',
        'density': 0.810,
        'useable': True
    },
    'hickory': {
        'class': 'wood',
        'toughness': 63.4,
        'strength': 15.59,
        'flexibility': 138.6,
        'rarity': 'common',
        'density': 0.835,
        'useable': True
    },
    'oak': {
        'class': 'wood',
        'toughness': 50.8,
        'strength': 12.15,
        'flexibility': 102.3,
        'rarity': 'abundant',
        'density': 0.755,
        'useable': True
    },
    'maple': {
        'class': 'wood',
        'toughness': 54.0,
        'strength': 12.62,
        'flexibility': 109.0,
        'rarity': 'common',
        'density': 0.705,
        'useable': True
    },
    'yew': {
        'class': 'wood',
        'toughness': 55.9,
        'strength': 9.10,
        'flexibility': 104.8,
        'rarity': 'rare',
        'density': 0.675,
        'useable': True
    },
    'elm': {
        'class': 'wood',
        'toughness': 31.3,
        'strength': 7.23,
        'flexibility': 62.0,
        'rarity': 'abundant',
        'density': 0.570,
        'useable': True
    },
    'ash': {
        'class': 'wood',
        'toughness': 51.1,
        'strength': 12.00,
        'flexibility': 103.5,
        'rarity': 'abundant',
        'density': 0.675,
        'useable': True
    },
    'linen': {
        'class': 'fiber',
        'density': 1.6,
        'toughness': 1500.0,
        'strength': 40.0,
        'flexibility': .04,
        'rarity': 'common',
        'useable': True
    },
    'cotton': {
        'class': 'fiber',
        'density': 1.54,
        'toughness': 850.0,
        'strength': 8.0,
        'rarity': 'abundant',
        'flexibility': .08,
        'useable': True
    },
    'hemp': {
        'class': 'fiber',
        'density': 1.49,
        'toughness': 696.0,
        'strength': 90.0,
        'rarity': 'abundant',
        'flexibility': .06,
        'useable': True
    },
    'shale': {
        'class': 'stone',
        'toughness': 475.0,
        'strength': 60.0,
        'flexibility': 1600.0,
        'rarity': 'common',
        'density': 2.75,
        'useable': True
    },
    'granite': {
        'class': 'stone',
        'toughness': 825.0,
        'strength': 70.0,
        'flexibility': 24000.0,
        'rarity': 'common',
        'density': 2.65,
        'useable': True
    },
    'sandstone': {
        'class': 'stone',
        'toughness': 805.0,
        'strength': 20.0,
        'flexibility': 400.0,
        'rarity': 'common',
        'density': 2.2,
        'useable': True
    },
    'marble': {
        'class': 'stone',
        'toughness': 190.0,
        'strength': 54.0,
        'flexibility': 27000.0,
        'rarity': 'common',
        'density': 2.7,
        'useable': True
    },
    'limestone': {
        'class': 'stone',
        'toughness': 238.0,
        'strength': 45.0,
        'flexibility': 24000.0,
        'rarity': 'common',
        'density': 2.45,
        'useable': True
    },
    'coal': {
        'class': 'stone',
        'rarity': 'common',
        'useable': False,
        'material yielded': 'steel'
    },
    'iron ore': {
        'class': 'metal',
        'rarity': 'abundant',
        'useable': False,
        'material yielded': 'iron'
    },
    'copper ore': {
        'class': 'metal',
        'rarity': 'common',
        'useable': False,
        'material yielded': 'copper'
    },
    'tin ore': {
        'class': 'metal',
        'rarity': 'rare',
        'useable': False,
        'material yielded': 'tin'
    },
    'silver ore': {
        'class': 'metal',
        'rarity': 'rare',
        'useable': False,
        'material yielded': 'silver'
    },
    'flax': {
        'class': 'metal',
        'rarity': 'common',
        'useable': False,
        'material yielded': 'linen'
    },
    'cotton boll': {
        'class': 'metal',
        'rarity': 'common',
        'useable': False,
        'material yielded': 'cotton'
    },
    'copper': {
        'class': 'metal',
        'toughness': 369.0,
        'strength': 119.0,
        'flexibility': 44700.0,
        'density': 8.96,
        'useable': True
    },
    'tin': {
        'class': 'metal',
        'toughness': 78.46,
        'strength': 50.0,
        'flexibility': 18000.0,
        'density': 7.365,
        'useable': True
    },
    'bronze': {
        'class': 'metal',
        'toughness': 980.7,
        'strength': 108.0,
        'flexibility': 44800,
        'density': 8.70
    },
    'silver': {
        'class': 'metal',
        'toughness': 251.0,
        'strength': 76.0,
        'flexibility': 30000.0,
        'density': 10.49,
        'useable': True
    },
    'gold': {
        'class': 'metal',
        'toughness': 216.0,
        'strength': 83.0,
        'flexibility': 27000.0,
        'rarity': 'very rare',
        'density': 19.30,
        'useable': True
    },
    'iron': {
        'class': 'metal',
        'toughness': 608.0,
        'strength': 211.0,
        'flexibility': 41000.0,
        'density': 7.874,
        'useable': True
    },
    'steel': {
        'class': 'metal',
        'toughness': 1373.0,
        'strength': 200.0,
        'flexibility': 79300.0,
        'density': 7.95,
        'useable': True
    },
    'silverine': {
        'class': 'metal',
        'toughness': 970.0,
        'strength': 110.3,
        'flexibility': 41000.0,
        'rarity': 'extremely rare',
        'density': 4.506,
        'useable': True
    },
    'adamantine steel': {
        'class': 'metal',
        'toughness': 8826.0,
        'strength': 120.0,
        'flexibility': 42000.0,
        'density': 7.777,
        'useable': True
    }
}


material_class_dct = {
    'wood': {
        'types': [],
        'trait factor': {
            'toughness': 1.0,
            'strength': 1.0,
            'flexibility': 1.0
        }
    },
    'fiber': {
        'types': [],
        'trait factor': {
            'toughness': 1.0,
            'strength': 1.0,
            'flexibility': 1.0
        }
    },
    'stone': {
        'types': [],
        'trait factor': {
            'toughness': 1.0,
            'strength': 1.0,
            'flexibility': 1.0
        }
    },
    'metal': {
        'types': [],
        'trait factor': {
            'toughness': 1.0,
            'strength': 1.0,
            'flexibility': 1.0
        }
    }
}
for material_type in material_type_dct.keys():
    material_class = material_type_dct[material_type]['class']
    if material_class not in material_class_dct.keys():
        material_class_dct[material_class] = []
    material_class_dct[material_class]['types'].append(material_type)
del material_type, material_class


occupation_type_dct = {
    'adventurer': {
        'material requirements': {
            'toughness': 2.5,
            'strength': 2.5,
            'flexibility': 1.5,
        }
    },
    'farmer': {
        'material requirements': {
            'toughness': 1.5,
            'strength': 2.5,
            'flexibility': 1.5,
        },
    },
    'miner': {
        'material requirements': {
            'toughness': 2.5,
            'strength': 2.5,
            'flexibility': 2.5,
        },
    },
    'woodcutter': {
        'material requirements': {
            'toughness': 2.5,
            'strength': 2.5,
            'flexibility': 1.0,
        },
    },
    'artisan': {
        'material requirements': {
            'toughness': 2.5,
            'strength': 1.0,
            'flexibility': 1.5,
        },
    },
    'homekeeper': {
        'material requirements': {
            'toughness': 1.0,
            'strength': 1.0,
            'flexibility': 2.5,
        },
    },
    'government': {
        'material requirements': {
            'toughness': 1.0,
            'strength': 1.5,
            'flexibility': 1.0,
        },
    },
    'retail': {
        'material requirements': {
            'toughness': 1.5,
            'strength': 1.5,
            'flexibility': 1.5,
        }
    }
}



monster_type_dct = {
    'lich': {
        'class': 'undead'
    },
    'warlock': {
        'class': 'magic'
    },
    'dragon': {
        'class': 'demon'
    }
}

monster_class_dct = {}
for monster_type in monster_type_dct.keys():
    monster_class = monster_type_dct[monster_type]['class']
    if monster_class not in monster_class_dct.keys():
        monster_class_dct[monster_class] = []
    monster_class_dct[monster_class].append(monster_type)
del monster_type, monster_class





terrain_dct = {
    1: {
        'terrain type': 'grassland',
        'console representation': '43m  ', 
        'image file': 'grassland_tile.png'
    },
    2: {
        'terrain type': 'woodland',
        'console representation': '42m  ',
        'image file': 'woodland_tile.png'
    },
    3: {
        'terrain type': 'rockland',
        'console representation': '47m  ',
        'image file': 'rockland_tile.png' 
    },
    't': {
        'terrain type': 'town',
        'console representation': '37;40m[]',
        'image file': 'town_tile.png'
    }
}

terrain_type_list = []
for terrain in [x for x in terrain_dct.keys() if type(x) == int]:
    terrain_type_list.append(terrain)


structure_type_dct = {
    'farm': {
        'class': 'grassland',
        'worker type': 'farmer',
        'worker capacity': 10,
        'site type': 'resource',
        'resource type': 'fiber',
        'time per harvest': 120,
        'transformations': ['fallow ground'],
        'image file': 'farm_tile.png'
    },
    'sawmill': {
        'class': 'woodland',
        'worker type': 'woodcutter',
        'worker capacity': 10,
        'site type': 'resource',
        'resource type': 'wood',
        'time per harvest': 350,
        'image file': 'sawmill_tile.png'
    },
    'mine': {
        'class': 'rockland',
        'worker type': 'miner',
        'worker capacity': 10,
        'site type': 'resource',
        'resource type': 'metal',
        'time per harvest': 600,
        'transformations': ['abandoned mine', 'collapsed mine'],
        'image file': 'mine_tile.png'
    },
    'dungeon': {
        'class': 'grassland',
        'worker type': 'adventurer',
        'worker capacity': 10,
        'site type': 'adventure',
        'time per harvest': 800,
        'image file': 'placeholder_tile.png'
    },
    'cave': {
        'class': 'rockland',
        'worker type': 'adventurer',
        'worker capacity': 10,
        'site type': 'adventure',
        'time per harvest': 100,
        'image file': 'placeholder_tile.png'
    },
    'tower': {
        'class': 'woodland',
        'worker type': 'adventurer',
        'worker capacity': 10,
        'site type': 'adventure',
        'time per harvest': 480,
        'image file': 'placeholder_tile.png'
    },
    'fallow ground': {
        'class': 'transformed',
        'worker type': 'adventurer',
        'worker capacity': 10,
        'site type': 'adventure',
        'time per harvest': 30,
        'transformations': ['farm'],
        'image file': 'placeholder_tile.png'
    },
    'abandoned mine': {
        'class': 'transformed',
        'worker type': 'adventurer',
        'worker capacity': 10,
        'site type': 'adventure',
        'time per harvest': 200,
        'transformations': ['collapsed mine'],
        'image file': 'placeholder_tile.png'
    },
    'collapsed mine': {
        'class': 'transformed',
        'site type': 'resource',
        'image file': 'placeholder_tile.png'
    }
}


structure_class_dct = {}
site_type_dct = {}
for structure_type in structure_type_dct.keys():
    structure_class = structure_type_dct[structure_type]['class']
    if structure_class not in structure_class_dct.keys():
        structure_class_dct[structure_class] = []
    structure_class_dct[structure_class].append(structure_type)
    site_type = structure_type_dct[structure_type]['site type']
    if site_type not in site_type_dct.keys():
        site_type_dct[site_type] = []
    site_type_dct[site_type].append(structure_type)
del structure_type, structure_class, site_type


rarity_dct = {
    'abundant': 200,
    'common': 100,
    'rare': 35,
    'very rare': 7,
    'extremely rare': 1
}


letter_dct = {
    'monster': {
        'consonant start': [
            'b', 'bl', 'br',
            'c', 'ch', 'chr', 'cl', 'cr',
            'd', 'dr',
            'f', 'fl', 'fr',
            'g', 'gh', 'ghr', 'gl', 'gr', 'gw', 
            'h',
            'j',
            'k', 'kh', 'khr', 'kl', 'kr', 'kw',
            'l',
            'm',
            'n', 'ng',
            'p', 'ph', 'phr', 'phl', 'pl', 'pr', 'ps',
            'q', 'qu',
            'r', 'rh',
            's', 'sc', 'sch', 'scr', 'sh', 'shr', 'sk', 'skr', 'sl', 'sm', 
                 'sn', 'sp', 'spl', 'spr', 'st', 'str', 'sv', 'sw',
            't', 'th', 'thr', 'tr', 'ts', 'tw',
            'v', 'vl',
            'w', 
            'x', 
            'y', 
            'z'
        ],
        'vowel start': [
            'a', 'aa', 'ae', 'ai', 'au',
            'e', 'ea', 'eu',
            'i', 'io',
            'o', 'oa', 'ou',
            'u'
        ],
        'consonant end': [
            'b', 'bs', 
            'c', 'ch', 'ck', 'cks',
            'd', 'ds', 'dge', 'dges', 'dgy', 
            'f', 'fs', 
            'g', 'gs',  
            'k', 'ks', 
            'l', 'ls', 
            'm', 'ms', 
            'n', 'ng', 'ngs', 'ns', 
            'p', 'ph', 'ps', 
            'qu', 
            'r',  'rs', 
            's', 'sc', 'sch', 'sh', 'sk', 'sm', 'sp', 'st',
            't', 'th', 'ts',
            'v',  
            'w', 
            'x', 
            'y',
            'z', 
        ],
        'vowel mid': [
        'a', 'ae', 'ai', 'au',
        'e', 'ea', 'eau', 'ee', 'ei', 'eo', 'eu',
        'i', 'ia', 'ie', 'io', 'iu',
        'o', 'oa', 'oe', 'oh', 'oi', 'oo', 'ou',
        'u', 'ua', 'ue', 'ui', 'uo', 'uu',
        'y',
        ]
    },
    'human': {
        'consonant start': [
            'b', 'c', 'ch', 'd', 
            'f', 'fr', 'g', 'gw', 
            'h','j', 'k', 'kr', 
            'l', 'm', 'n', 'p',
            'r', 's', 'sh', 'sm', 
            'st', 't', 'th', 'tr',
            'v', 'w'
        ],
        'vowel start': [
            'a',
            'e',
            'i',
        ],
        'consonant end': [
            'b', 
            'c', 'ch', 'ck', 
            'd', 
            'f',
            'g', 
            'k', 
            'l',
            'm', 
            'n', 
            'p',
            'r',
            's', 'sh', 'st',
            't', 'th', 
            'x', 
            'z', 
        ],
        'vowel mid': [
        'a', 
        'e', 'ea', 'eau', 
        'i', 'ia', 
        'o', 'oh', 'oo',
        'u', 
        'y',
        ]
    }
}
