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


#TODO: Once a weapon of every class exists, weapon_class_dct may be 
#generated with an init function on weapon_type_dct.
#Hardcoded data just for reference right now.
weapon_class_dct = {
    'dagger': [
        'dirk'
    ],
    'sword': [
        'shortsword',
        'longsword'
    ],
    'blunt': [
        'flail',
        'double flail'
    ],
    'cleave': [
        'battle axe'
    ],
    'polearm': [
    
    ],
    'bow': [
    
    ],
    'ammunition': [
    
    ],
    'projectile': [
    
    ]
}


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


#TODO: like weapon_class_dct, make be generated
component_class_dct = {
    'base': [
    
    ],
    'edge': [
    
    ],
    'flagellum': [
    
    ],
    'finger': [
    
    ],
    'extension': [
    
    ],
    'string': [
    
    ],
    'standalone': [
    
    ]
}


#Density measured in g·cm−3
material_type_dct = {
    'bodark': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'epay': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'lemonwood': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'pignut': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'hickory': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'oak': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'maple': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'yew': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'elm': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'ash': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None,
        'intrinsic value': None
    },
    'linen': {
        'class': 'fiber',
        'intrinsic value': None
    },
    'hemp': {
        'class': 'fiber',
        'intrinsic value': None
    },
    'sinew': {
        'class': 'fiber',
        'intrinsic value': None
    },
    'silk': {
        'class': 'fiber',
        'intrinsic value': None
    },
    'rawhide': {
        'class': 'fiber',
        'intrinsic value': None
    },
    'chert': {
        'class': 'stone',
        'intrinsic value': None
    },
    'flint': {
        'class': 'stone',
        'intrinsic value': None
    },
    'granite': {
        'class': 'stone',
        'intrinsic value': None
    },
    'marble': {
        'class': 'stone',
        'intrinsic value': None
    },
    'cow leather': {
        'class': 'leather',
        'intrinsic value': None
    },
    'buffalo leather': {
        'class': 'leather',
        'intrinsic value': None
    },
    'goat hide': {
        'class': 'leather',
        'intrinsic value': None
    },
    'calfskin': {
        'class': 'leather',
        'intrinsic value': None
    },
    'sheepskin': {
        'class': 'leather',
        'intrinsic value': None
    },
    'deerskin': {
        'class': 'leather',
        'intrinsic value': None
    },
    'elkskin': {
        'class': 'leather',
        'intrinsic value': None
    },
    'horse leather': {
        'class': 'leather',
        'intrinsic value': None
    },
    'sharkskin': {
        'class': 'leather',
        'intrinsic value': None
    },
    'dragonhide': {
        'class': 'leather',
        'intrinsic value': None
    },
    'copper': {
        'class': 'metal',
        'rarity': 60.0,
        'density': 8.96,
        'intrinsic value': None
    },
    'bronze': {
        'class': 'metal',
        'rarity': None,
        'density': 8.70,
        'intrinsic value': None
    },
    'silver': {
        'class': 'metal',
        'rarity': 0.075,
        'density': 10.49,
        'intrinsic value': None
    },
    'gold': {
        'class': 'metal',
        'rarity': 0.004,
        'density': 19.30,
        'intrinsic value': None
    },
    'iron': {
        'class': 'metal',
        'rarity': 56300.0,
        'density': 7.874,
        'intrinsic value': None
    },
    'steel': {
        'class': 'metal',
        'rarity': None,
        'density': 7.95,
        'intrinsic value': None
    },
    'silverine': {
        'class': 'metal',
        'rarity': 0.001,
        'density': 4.506,
        'instrinsic value': None
    },
    'adamantine steel': {
        'class': 'metal',
        'density': 7.777,
        'intrinsic value': None
    }
}

#TODO: like weapon_class_dct, make be generated
material_class_dct = {
    'wood': [
        'bodark',
        'epay',
        'lemonwood',
        'pignut',
        'hickory',
        'oak',
        'maple',
        'yew',
        'elm',
        'ash'
    ],
    'fiber': [
        'linen',
        'hemp',
        'sinew',
        'silk',
        'rawhide'
    ],
    'stone': [
        'chert',
        'flint',
        'granite',
        'marble'
    ],
    'leather': [
        'cow leather',
        'buffalo leather',
        'goat hide',
        'calfskin',
        'sheepskin',
        'deerskin',
        'elkskin',
        'horse leather',
        'sharkskin',
        'dragonhide'
    ],
    'metal': [
        'copper',
        'bronze',
        'silver',
        'gold',
        'iron',
        'steel',
        'silvered steel',
        'adamantine steel'
    ]
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
