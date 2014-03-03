import entities
from random import choice


class Weapon():

    weapon_type_dct = {
        'dirk': {
            'class': 'dagger',
            'component': ['hilt', 'blade', 'scabbard'],
            'hands to wield': 1
        },
        'shortsword': {
            'class': 'sword',
            'component': ['hilt', 'blade', 'scabbard'],
            'hands to wield': 1
        },
        'longsword': {
            'class': 'sword',
            'component': ['hilt', 'blade', 'scabbard'],
            'hands to wield': 2
        }
    }

    #TODO: Once a weapon of every class exists, weapon_class_dct may be generated with an init function on weapon_type_dct.
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
        
        ],
        'cleave': [
        
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
        self.components = []
        
    def print_stats(self):
        """Prints the weapon's information in the console."""
        print "\nWeapon ID:         %r" % self.weapon_id
        print "Weapon type:       %s" % self.weapon_type
        print "Weapon class:      %s" % self.weapon_class
        print "Weapon components:"
        for component in self.components:
            print "    %s:" % component.component_type
            for material in component.materials:
                print "        %s (%s)" % (
                    material.material_type, material.material_class)
        print "\n"

    def generate(self, arg='random'):
        if arg == 'random':
            self.weapon_type = choice(Weapon.weapon_type_dct.keys())
            self.weapon_class = Weapon.weapon_type_dct[
                                        self.weapon_type]['class']
            for component in Weapon.weapon_type_dct[
                    self.weapon_type]['component']:
                self.components.append(
                        Component().generate(component))
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
        }
    }

    def __init__(self):
        self.component_type = None
        self.materials = []

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


class Material():

    material_class_dct = {
        'wood': {
            'type': {
                'hickory': {},
                'ash': {}
            } 
        },
        'fiber': {
            'type': {
                'linen': {},
                'hemp': {},
                'sinew': {}
            }
        },
        'stone': {
            'type': {
                'granite': {},
                'marble': {}
            }
        },
        'leather': {
            'type': {
                'cow leather': {},
                'goat leather': {}
            }
        },
        'metal': {
            'type': {
                'copper': {},
                'bronze': {},
                'iron': {},
                'steel': {}
            }
        }
    }

    def __init__(self):
        self.material_class = None
        self.material_type = None
    
    def generate(self, material_class, arg='random'):
        self.material_class = material_class
        if arg == 'random':
            self.material_type = choice(
                            Material.material_class_dct[
                                material_class]['type'].keys())
        else:
            return NotImplementedError(arg)
        return self
