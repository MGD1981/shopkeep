import entities
import reference_data as ref
from random import choice, randint


class Weapon():
    """Weapon class object with unique weapon_id.  Contains Component objects."""

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
        """Generates a random weapon from reference_data.weapon_type_dct."""
        if arg == 'random':
            self.weapon_type = choice(ref.weapon_type_dct.keys())
            self.weapon_class = ref.weapon_type_dct[
                                        self.weapon_type]['class']
            for component in ref.weapon_type_dct[
                    self.weapon_type]['components']:
                self.components.append(
                        Component().generate(component))
            self.assemble(self.weapon_type, self.components)
        else:
            return NotImplementedError(arg)
        return self
        
        
    def assemble(weapon_type, component_list):
        """Joint generation & connection function."""
        joining_table = {}         
        
        components_to_connect = ref.weapon_type_dct[
                                self.weapon_type]['components']
        n = 0
        for c in components_to_connect:
            n += ref.component_type_dct[c]['number of joints']
        number_of_joints_to_connect = n/2
        components_connected = []
        joints_to_connect = []
        for x in xrange(number_of_joints_to_connect):
            joints_to_connect.append(Joint().generate())
#        for component_to_connect in components_to_connect:
#            for component in self.components:
#                if component.component_type == component_to_connect:
                    #connect if not already connected
                    #test if connected:
                    #TODO: Build some helper functions


class Component():
    """Component object class with unique component ID.
       Contains Material objects and Joint objects."""

    def __init__(self):
        self.component_id = None
        self.component_type = None
        self.materials = []
        self.joints = []

    def generate(self, component_type, arg='random'):
        if arg == 'random':
            self.component_type = component_type
            self.materials.append(
                    Material().generate(choice(
                    ref.component_type_dct[
                    component_type]['possible materials'])))
        else:
            return NotImplementedError(arg)
        return self


class Joint():
    """Joint object class.  May exist as attribute of multiple Component objects."""

    def __init__(self):
        self.material = None #material of which joint is made
        self.material_integrity = None #i.e. 100=new, 0=broken
        self.joint_quality = None #higher quality = slower rate of deterioration
        self.joint_integrity = None #i.e. 100-new, 0=broken
        self.components_joined = []

    def join(components):
        """Joins a list of Component objects."""
        if len(components_joined != 0):
            print "Joint already connected."
            return
        try:
            if len(set(components)) != len(components):
                print "Cannot join component to itself."
                return
            for component in components:
                component.joints.append(self)
                self.components_joined.append(component)
            return
        except AttributeError:
            print "Failed joining invalid components"
            return

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
    """Material object class."""

    def __init__(self):
        self.material_class = None
        self.material_type = None
        self.material_quality = None
    
    def generate(self, material_class, arg='random'):
        self.material_class = material_class
        if arg == 'random':
            self.material_type = choice(
                            ref.material_class_dct[
                                material_class]['type'].keys())
        else:
            return NotImplementedError(arg)
        return self
