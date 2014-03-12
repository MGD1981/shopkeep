weapon_type_dct = {
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
#Hardness in lbf
#Strength in GPa
#Flexibility in MPa
material_type_dct = {
    'bodark': {
        'class': 'wood',
        'hardness': 2760,
        'strength': 11.64,
        'flexibility': 128.6,
        'rarity': 'common',
        'density': 0.855,
    },
    'ipay': {
        'class': 'wood',
        'hardness': 3510,
        'strength': 22.07,
        'flexibility': 177.0,
        'rarity': 'rare',
        'density': 1.100,
    },
    'lemonwood': {
        'class': 'wood',
        'hardness': 1880,
        'strength': 15.75,
        'flexibility': 152.4,
        'rarity': 'very rare',
        'density': 0.810,
    },
    'hickory': {
        'class': 'wood',
        'hardness': 2140,
        'strength': 15.59,
        'flexibility': 138.6,
        'rarity': 'common',
        'density': 0.835,
    },
    'oak': {
        'class': 'wood',
        'hardness': 1350,
        'strength': 12.15,
        'flexibility': 102.3,
        'rarity': 'abundant',
        'density': 0.755,
    },
    'maple': {
        'class': 'wood',
        'hardness': 1450,
        'strength': 12.62,
        'flexibility': 109.0,
        'rarity': 'common',
        'density': 0.705,
    },
    'yew': {
        'class': 'wood',
        'hardness': 1520,
        'strength': 9.10,
        'flexibility': 104.8,
        'rarity': 'rare',
        'density': 0.675,
    },
    'elm': {
        'class': 'wood',
        'hardness': 800,
        'strength': 7.23,
        'flexibility': 62.0,
        'rarity': 'abundant',
        'density': 0.570,
    },
    'ash': {
        'class': 'wood',
        'hardness': 1320,
        'strength': 12.00,
        'flexibility': 103.5,
        'rarity': 'abundant',
        'density': 0.675,
    },
    'linen': {
        'class': 'fiber',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'hemp': {
        'class': 'fiber',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'sinew': {
        'class': 'fiber',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'silk': {
        'class': 'fiber',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'rawhide': {
        'class': 'fiber',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'chert': {
        'class': 'stone',
        'hardness': 7.0,
        'strength': None,
        'flexibility': 'brittle',
        'rarity': None,
        'density': 2.65,
    },
    'flint': {
        'class': 'stone',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': 2.6,
    },
    'granite': {
        'class': 'stone',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': 2.65,
    },
    'marble': {
        'class': 'stone',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': 2.55,
    },
    'cow leather': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'buffalo leather': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'goat hide': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'calfskin': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'sheepskin': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'deerskin': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'elkskin': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'horse leather': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'sharkskin': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'dragonhide': {
        'class': 'leather',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': None,
    },
    'copper': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': 60.0,
        'density': 8.96,
    },
    'tin': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': 2.3,
        'density': 7.365,
    },
    'bronze': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': 8.70,
    },
    'silver': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': 0.075,
        'density': 10.49,
    },
    'gold': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': 0.004,
        'density': 19.30,
    },
    'iron': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': 56300.0,
        'density': 7.874,
    },
    'steel': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': None,
        'density': 7.95,
    },
    'silverine': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'rarity': 0.001,
        'density': 4.506,
    },
    'adamantine steel': {
        'class': 'metal',
        'hardness': None,
        'strength': None,
        'flexibility': None,
        'density': 7.777,
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
