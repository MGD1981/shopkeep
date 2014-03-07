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


material_type_dct = {
    'bodark': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'epay': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'lemonwood': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'pignut': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'hickory': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'oak': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'maple': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'yew': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'elm': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'ash': {
        'class': 'wood',
        'strength': None,
        'flexibility': None,
        'density': None
    },
    'linen': {
        'class': 'fiber'
    },
    'hemp': {
        'class': 'fiber'
    },
    'sinew': {
        'class': 'fiber'
    },
    'silk': {
        'class': 'fiber'
    },
    'rawhide': {
        'class': 'fiber'
    },
    'chert': {
        'class': 'stone'
    },
    'flint': {
        'class': 'stone'
    },
    'granite': {
        'class': 'stone'
    },
    'marble': {
        'class': 'stone'
    },
    'cow leather': {
        'class': 'leather'
    },
    'buffalo leather': {
        'class': 'leather'
    },
    'goat hide': {
        'class': 'leather'
    },
    'calfskin': {
        'class': 'leather'
    },
    'sheepskin': {
        'class': 'leather'
    },
    'deerskin': {
        'class': 'leather'
    },
    'elkskin': {
        'class': 'leather'
    },
    'horse leather': {
        'class': 'leather'
    },
    'sharkskin': {
        'class': 'leather'
    },
    'dragonhide': {
        'class': 'leather'
    },
    'copper': {
        'class': 'metal'
    },
    'bronze': {
        'class': 'metal'
    },
    'silver': {
        'class': 'metal'
    },
    'gold': {
        'class': 'metal'
    },
    'iron': {
        'class': 'metal'
    },
    'steel': {
        'class': 'metal'
    },
    'silvered steel': {
        'class': 'metal'
    },
    'adamantine steel': {
        'class': 'metal'
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
}
