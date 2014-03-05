import entities
from random import choice, randint


class Weapon():

    #TODO: Move dct reference objects to dct class
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

    def __init__(self):
        self.weapon_id = None #TODO: get unique based on entities.weapons
        self.weapon_type = None
        self.weapon_class = None
        self.owners = []
        self.kills = []
        self.components = [] #Each component has Joint objects connecting it.
        
    def print_stats(self):
        """Prints the weapon's information in the console."""
        print "\nWeapon ID:         %r" % self.weapon_id
        print "Weapon type:       %r" % self.weapon_type
        print "Weapon class:      %r" % self.weapon_class
        print "Weapon components:"
        for component in self.components:
            print "    %r:" % component.component_type
            for material in component.materials:
                print "        %r (%r)" % (
                    material.material_type, material.material_class)
#            for joint in component.joints:
#                joined = None
#                for c in self.components:
#                    if joint in c.joints and c != component:
#                        joined = c
#                        break
#                print "        with a %r joint connecting to the %r." (
#                    joint.material.material_type, joined.component_type)
        print "\n"

    def generate(self, arg='random'):
        if arg == 'random':
            self.weapon_type = choice(Weapon.weapon_type_dct.keys())
            self.weapon_class = Weapon.weapon_type_dct[
                                        self.weapon_type]['class']
            for component in Weapon.weapon_type_dct[
                    self.weapon_type]['components']:
                self.components.append(
                        Component().generate(component))
            components_to_connect = Weapon.weapon_type_dct[
                                    self.weapon_type]['components']
            n = 0
            for c in components_to_connect:
                n += len(components_to_connect[c]['joints'])
            number_of_joints_to_connect = n/2
            components_connected = []
            joints_to_connect = []
            for x in xrange(number_of_joints_to_connect):
                joints_to_connect.append(Joint().generate())
#            for component_to_connect in components_to_connect:
#                for component in self.components:
#                    if component.component_type == component_to_connect:
                        #connect if not already connected
                        #test if connected:
                        #TODO: Build some helper functions


            
        else:
            return NotImplementedError(arg)
        return self


class Component():

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

    def __init__(self):
        self.component_type = None
        self.materials = []
        self.joints = []

    def generate(self, component_type, arg='random'):
        if arg == 'random':
            self.component_type = component_type
            self.materials.append(
                    Material().generate(choice(
                    Component.component_type_dct[
                    component_type]['possible materials'])))
        else:
            return NotImplementedError(arg)
        return self


class Joint():

    def __init__(self):
        self.material = None #material of which joint is made
        self.material_integrity = None #i.e. 100=new, 0=broken
        self.joint_quality = None #higher quality = slower rate of deterioration
        self.joint_integrity = None #i.e. 100-new, 0=broken

    def generate(self, arg='random'):
        if arg == 'random':
            self.material = Material().generate('metal')
            self.material_integrity = randint(1,100)
            self.joint_quality = randint(1,100)
            self.joint_integrity = randint(1,100)
        else:
            return NotImplementedError(arg)
        return self
        
        

class Material():

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

    def __init__(self):
        self.material_class = None
        self.material_type = None
        self.material_quality = None
    
    def generate(self, material_class, arg='random'):
        self.material_class = material_class
        if arg == 'random':
            self.material_type = choice(
                            Material.material_class_dct[
                                material_class]['type'].keys())
        else:
            return NotImplementedError(arg)
        return self
