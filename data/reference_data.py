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


component_type_dct = {
    'shaft': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': [('multi', 'point')]
    },
    'head': {
        'class': 'point',
        'possible materials': ['stone', 'metal'],
        'joints': [('single', 'point')]
    },
    'hilt': {
        'class': 'base',
        'possible materials': ['wood', 'stone', 'metal'],
        'joints': [('single', 'edge')]
    },
    'blade': {
        'class': 'edge',
        'possible materials': ['metal'],
        'joints': [('single', 'base')]
    },
    'scabbard': {
        'class': 'standalone',
        'possible materials': ['leather', 'wood', 'metal'],
        'joints': []
    },
    'haft': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': [('multi', 'edge')]
    },
    'handle': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': [('multi', 'flagellum')]
    },
    'chain': {
        'class': 'flagellum',
        'possible materials': ['metal'],
        'joints': [('single', 'base'), ('optional', 'finger')]
    },
    'ball': {
        'class': 'finger',
        'possible materials': ['metal'],
        'joints': [('single', 'flagellum')]
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
material_type_dct = {
    'bodark': {
        'class': 'wood',
        'toughness': 64.7,
        'strength': 11.64,
        'flexibility': 128.6,
        'rarity': 'common',
        'density': 0.855
    },
    'ipay': {
        'class': 'wood',
        'toughness': 93.8,
        'strength': 22.07,
        'flexibility': 177.0,
        'rarity': 'rare',
        'density': 1.100
    },
    'lemonwood': {
        'class': 'wood',
        'toughness': 67.5,
        'strength': 15.75,
        'flexibility': 152.4,
        'rarity': 'very rare',
        'density': 0.810
    },
    'hickory': {
        'class': 'wood',
        'toughness': 63.4,
        'strength': 15.59,
        'flexibility': 138.6,
        'rarity': 'common',
        'density': 0.835
    },
    'oak': {
        'class': 'wood',
        'toughness': 50.8,
        'strength': 12.15,
        'flexibility': 102.3,
        'rarity': 'abundant',
        'density': 0.755
    },
    'maple': {
        'class': 'wood',
        'toughness': 54.0,
        'strength': 12.62,
        'flexibility': 109.0,
        'rarity': 'common',
        'density': 0.705
    },
    'yew': {
        'class': 'wood',
        'toughness': 55.9,
        'strength': 9.10,
        'flexibility': 104.8,
        'rarity': 'rare',
        'density': 0.675
    },
    'elm': {
        'class': 'wood',
        'toughness': 31.3,
        'strength': 7.23,
        'flexibility': 62.0,
        'rarity': 'abundant',
        'density': 0.570
    },
    'ash': {
        'class': 'wood',
        'toughness': 51.1,
        'strength': 12.00,
        'flexibility': 103.5,
        'rarity': 'abundant',
        'density': 0.675
    },
    'linen': {
        'class': 'fiber',
        'density': 1.6,
        'toughness': 1500.0,
        'strength': 40.0,
        'flexibility': .04,
        'rarity': None
    },
    'cotton': {
        'class': 'fiber',
        'density': 1.54,
        'toughness': 850.0,
        'strength': 8.0,
        'flexibility': .08,
        'rarity': None
    },
    'hemp': {
        'class': 'fiber',
        'density': 1.49,
        'toughness': 696.0,
        'strength': 90.0,
        'flexibility': .06,
        'rarity': None
    },
    'shale': {
        'class': 'stone',
        'toughness': 475.0,
        'strength': 60.0,
        'flexibility': 1600.0,
        'rarity': None,
        'density': 2.75
    },
    'granite': {
        'class': 'stone',
        'toughness': 825.0,
        'strength': 70.0,
        'flexibility': 24000.0,
        'rarity': None,
        'density': 2.65
    },
    'sandstone': {
        'class': 'stone',
        'toughness': 805.0,
        'strength': 20.0,
        'flexibility': 400.0,
        'rarity': None,
        'density': 2.2
    },
    'marble': {
        'class': 'stone',
        'toughness': 190.0,
        'strength': 54.0,
        'flexibility': 27000.0,
        'rarity': None,
        'density': 2.7
    },
    'limestone': {
        'class': 'stone',
        'toughness': 238.0,
        'strength': 45.0,
        'flexibility': 24000.0,
        'rarity': None,
        'density': 2.45
    },
    'coal': {
        'class': 'resource',
        'rarity': None
    },
    'flax': {
        'class': 'resource',
        'rarity': None
    },
    'cotton boll': {
        'class': 'resource',
        'rarity': None
    },
    'cow leather': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'buffalo leather': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'goat hide': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'calfskin': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'sheepskin': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'deerskin': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'elkskin': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'horse leather': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'sharkskin': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'dragonhide': {
        'class': 'leather',
        'toughness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None
    },
    'copper': {
        'class': 'metal',
        'toughness': 369.0,
        'strength': 119.0,
        'flexibility': 44700.0,
        'rarity': 60.0,
        'density': 8.96
    },
    'tin': {
        'class': 'metal',
        'toughness': 78.46,
        'strength': 50.0,
        'flexibility': 18000.0,
        'rarity': 2.3,
        'density': 7.365
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
        'rarity': 0.075,
        'density': 10.49
    },
    'gold': {
        'class': 'metal',
        'toughness': 216.0,
        'strength': 83.0,
        'flexibility': 27000.0,
        'rarity': 0.004,
        'density': 19.30
    },
    'iron': {
        'class': 'metal',
        'toughness': 608.0,
        'strength': 211.0,
        'flexibility': 41000.0,
        'rarity': 56300.0,
        'density': 7.874
    },
    'steel': {
        'class': 'metal',
        'toughness': 1373.0,
        'strength': 200.0,
        'flexibility': 79300.0,
        'density': 7.95
    },
    'silverine': {
        'class': 'metal',
        'toughness': 970.0,
        'strength': 110.3,
        'flexibility': 41000.0,
        'rarity': 0.001,
        'density': 4.506
    },
    'adamantine steel': {
        'class': 'metal',
        'toughness': 8826.0,
        'strength': 120.0,
        'flexibility': 42000.0,
        'density': 7.777
    }
}


#TODO
for material_type in material_type_dct.keys():
    material_type_dct[material_type]['intrinsic value'] = 0


material_class_dct = {}
for material_type in material_type_dct.keys():
    material_class = material_type_dct[material_type]['class']
    if material_class not in material_class_dct.keys():
        material_class_dct[material_class] = []
    material_class_dct[material_class].append(material_type)
del material_type, material_class
 


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
