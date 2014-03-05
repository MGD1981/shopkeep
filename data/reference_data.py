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
        'joints': (('single', 'edge'))
    },
    'blade': {
        'class': 'edge',
        'possible materials': ['metal'],
        'joints': (('single', 'base'))
    },
    'scabbard': {
        'class': 'standalone',
        'possible materials': ['leather', 'wood', 'metal'],
        'joints': ()
    },
    'haft': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': (('multi', 'edge'))
    },
    'handle': {
        'class': 'base',
        'possible materials': ['wood'],
        'joints': (('multi', 'flagellum'))
    },
    'chain': {
        'class': 'flagellum',
        'possible materials': ['metal'],
        'joints': (('single', 'handle'), ('single', 'finger'))
    },
    'ball': {
        'class': 'finger',
        'possible materials': ['metal'],
        'joints': (('single', 'flagellum'))
    },
    'limb': {
        'class': 'extension',
        'possible materials': ['wood'],
        'joints': (('single', 'base'), ('single', 'string'))
    },
    'bowstring': {
        'class': 'string',
        'possible materials': ['fiber'],
        'joints': (('single', 'extension'), ('single', 'extension'))
    }
}


material_class_dct = {
    'wood': {
        'type': {
            'bodark': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'epay': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'lemonwood': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'pignut': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'hickory': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'oak': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'maple': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'yew': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'elm': {
                'strength': None,
                'flexibility': None,
                'density': None
            },
            'ash': {
                'strength': None,
                'flexibility': None,
                'density': None
            }
        } 
    },
    'fiber': {
        'type': {
            'linen': {},
            'hemp': {},
            'sinew': {},
            'silk': {},
            'rawhide': {}
        }
    },
    'stone': {
        'type': {
            'chert': {},
            'flint': {},
            'granite': {},
            'marble': {}
        }
    },
    'leather': {
        'type': {
            'cow leather': {},
            'buffalo leather': {},
            'goat hide': {},
            'calfskin': {},
            'sheepskin': {},
            'deerskin': {},
            'elkskin': {},
            'horse leather': {},
            'sharkskin': {},
            'dragonhide': {}
        }
    },
    'metal': {
        'type': {
            'copper': {},
            'bronze': {},
            'silver': {},
            'gold': {},
            'iron': {},
            'steel': {},
            'silvered steel': {},
            'adamantine steel': {}
        }
    }
}