

weapon_type_dct = {
    'dirk': {
        'class': 'dagger',
        'components': {
            'hilt': {
                'joints': ['blade']
            },
            'blade': {
                'joints': ['hilt']
            },
            'scabbard': {
                'joints': []
            },
        },
        'hands to wield': 1
    },
    'shortsword': {
        'class': 'sword',
        'components': {
            'hilt': {
                'joints': ['blade']
            },
            'blade': {
                'joints': ['hilt']
            },
            'scabbard': {
                'joints': []
            }
        },
        'hands to wield': 1
    },
    'longsword': {
        'class': 'sword',
        'components': {
            'hilt': {
                'joints': ['blade']
            },
            'blade': {
                'joints': ['hilt']
            },
            'scabbard': {
                'joints': []
            }
        },
        'hands to wield': 2
    },
    'flail': {
        'class': 'blunt',
        'components': {
            'handle': {
                'joints': ['chain']
            },
            'chain': {
                'joints': ['handle', 'ball']
            },
            'ball': {
                'joints': ['chain']
            }
        },
        'hands to wield': 1
    },
    'double flail': {
        'class': 'blunt',
        'components': {
            'handle': {
                'joints': ['chain', 'chain']
            },
            'chain': {
                'joints': ['handle', 'ball']
            },
            'ball': {
                'joints': ['chain']
            },
            'chain': {
                'joints': ['handle', 'ball']
            },
            'ball': {
                'joints': ['chain']
            }
        },
        'hands to wield': 1
    },
    'battle axe': {
        'class': 'cleave',
        'components': {
            'haft': {
                'joints': ['blade']
            },
            'blade': {
                'joints': ['haft'],
            }
        },
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
        'possible materials': ['wood', 'stone', 'metal']
    },
    'blade': {
        'possible materials': ['metal']
    },
    'scabbard': {
        'possible materials': ['leather', 'wood', 'metal']
    },
    'haft': {
        'possible materials': ['wood']
    },
    'handle': {
        'possible materials': ['wood']
    },
    'chain': {
        'possible materials': ['metal']
    },
    'ball': {
        'possible materials': ['metal']
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