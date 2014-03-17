import entities


class Monster():
    """Class holding unique hero object"""

    def __init__(self):
        self.monster_id = None #TODO: get unique based on entities.heroes
		self.monster_type = None
        self.location = [None, None]
        self.name = None
        self.kills = []
        self.size = 100 #represents percent of "normal" size


    def generate(self, arg='random'):
        """Generates a monster."""
        import language
        if arg == 'random':
            pass
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