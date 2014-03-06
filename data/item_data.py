import entities
import reference_data as ref
from random import choice, randint


class Weapon():
    """Weapon class object with unique weapon_id.  Contains Component objects."""


    def __init__(self):
        self.weapon_id = None
        self.weapon_type = None
        self.weapon_class = None
        self.owners = []
        self.kills = []
        self.components = [] #Each component has Joint objects connecting it.
        
        
    def get_mass(self):
        m = 0
        for component in self.components:
            v = component.component_volume
            d = component.materials[0] #TODO: Once components may contain
                                       #multiple materials, change calculation.
            m += d*v
        return m
        
        
    def get_volume(self):
        v = 0
        for component in self.components:
            v += component.component.volume
        return v


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
            for joint in component.joints:
                joined = None
                for c in self.components:
                    if joint in c.joints and c != component:
                        joined = c
                        break
                print "        with a %r joint connecting to the %r." (
                    joint.material.material_type, joined.component_type)
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
        self.set_weapon_id()
        return self
        
        
    def assemble(self, weapon_type, component_list):
        """Joint generation & connection function."""        
        
        joint_table = {}
        #Remove components without joints from component_list:
        component_types_to_connect = [
                c for c in ref.weapon_type_dct[weapon_type][
                'components'] if ref.component_type_dct[c][
                'class'] == 'standalone' ]
        for component in component_list:
            if component.component_type not in component_types_to_connect:
                component_list.remove(component)

        for component in component_list:
            joint_table[component.component_id] = {
                'component type': component.component_type,
                'component class': ref.component_type_dct[
                        component.component_type]['class'],
                'joined to': [],
                'joints remaining': ref.component_type_dct[
                        component.component_type]['joints']
            }
        #joint table now has a key for every component_id
        #key['joined to'] is list of (id, type) of connected components
        while any(len(joint_table[c.component_id]['joints remaining']) > 0 for c in component_list):
            #single joints first
            for component1 in component_list:
                for open_joint1 in joint_table[component1.component_id]['joints remaining']:
                    if open_joint1[0] == 'single':
                        for component2 in component_list:
                            if component2.component_id == component1.component_id:
                                next
                            if (joint_table[component2.component_id]['component class'] == open_joint1[1]:
                                try:
                                    open_joint2_index = joint_table[component2.component_id][
                                            'joints remaining'].index(('single', component1.component_class)):
                                except ValueError:
                                    next
                                Joint().generate().join(component1, component2)
                                joint_table[component1.component_id]['joints remaining'].remove(open_joint1)
                                joint_table[component2.component_id]['joints remaining'].remove(
                                        joint_table[component2.component_id]['joints remaining'][open_joint2_index])

        
                            
        return

                    
        

    def set_weapon_id(self):
        """Gives weapon object unique ID."""
        self.weapon_id = entities.weapons['next id']
        entities.weapons['object list'].append(self)
        entities.weapons['next id'] += 1
        return
        
        
    def __repr__(self):
        return 'Weapon(ID: %r, Type:%r)' % (self.weapon_id, self.weapon_type)



class Component():
    """Component object class with unique component ID.
       Contains Material objects and Joint objects."""


    def __init__(self):
        self.component_id = None
        self.component_type = None
        self.component_volume = None
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
        self.set_component_id()
        return self
        
        
    def set_component_id(self):
        """Gives component object unique ID."""
        self.component_id = entities.components['next id']
        entities.components['object list'].append(self)
        entities.components['next id'] += 1
        return
        
        
    def __repr__(self):
        return 'Component(ID: %r, Type:%r)' % (self.component_id, self.component_type)



class Joint():
    """Joint object class.  May exist as attribute of multiple Component objects."""


    def __init__(self):
        self.material = None #material of which joint is made
        self.material_integrity = None #i.e. 100=new, 0=broken
        self.joint_quality = None #higher quality = slower rate of deterioration
        self.joint_integrity = None #i.e. 100-new, 0=broken
        self.components_joined = []


    def join(component_list):
        """Joins a list of Component objects."""
        if len(components_joined != 0):
            print "Joint already connected."
            return
        try:
            if len(set(component_list)) != len(component_list):
                print "Cannot join component to itself."
                return
            for component in component_list:
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
        self.material_density = None
    
    
    def generate(self, material_class, arg='random'):
        self.material_class = material_class
        if arg == 'random':
            self.material_type = choice(
                            ref.material_class_dct[
                                material_class]['type'].keys())
        else:
            return NotImplementedError(arg)
        return self
