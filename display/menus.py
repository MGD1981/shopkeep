

class Option:
    """Menu option class."""

    def __init__(self):
        self.text = None #text to display in the menu
        self.actions = None #list of strings to be exec'd
        self.return_value = None #value to be returned after actions


class Menu:
    """Menu class."""

    def __init__(self):
        self.options = []


class StartMenu(Menu):

    def __init__(self):
        Menu.__init__(self)

        o1 = Option()
        o1.text = "Start New Game"
        o1.actions = [
                      'print "Initializing entities..."',
                      'data.entities.initialize()',
                      'game.screens["world"].initialize_sprites(game)'
                     ]

        o2 = Option()
        o2.text = "Continue Saved Game"
        o2.actions = [
                      'run_menu(game, menus.ContinueGameMenu())'
                     ]

        o3 = Option()
        o3.text = "Quit"
        o3.actions = [
                      'print "Thanks for playing!"',
                      'pg.quit()'
                     ]

        self.options.extend([o1,o2,o3])
