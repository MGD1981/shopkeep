import entities
import reference_data as ref
from random import choice


class Monster():
    """Class holding unique hero object"""

    def __init__(self):
        self.monster_id = None #TODO: get unique based on entities.heroes
		self.monster_type = None
        self.location = [None, None]
        self.name = None
        self.kills = []
        self.size = 100 #represents percent of "normal" size


    def generate(self, monster_class='random', arg='random'):
        """Generates a monster."""
        import language
        if monster_class = 'random':
            monster_class = choice(ref.monster_type_dct.keys())
        if arg == 'random':
            self.monster_type = choice(ref.monster_class_dct[monster_class])
        self.name = language.create_name('monster')
        self.set_monster_id()
        return self


    def set_monster_id(self):
        """Gives monster object uniquue ID."""
        self.monster_id = entities.monsters['next id']
        entities.monsters['object list'].append(self)
        entities.monsters['next id'] += 1
		

    def __repr__(self):
        return 'Monster(ID: %r, Name:%r)' % (self.monster_id, self.name)
