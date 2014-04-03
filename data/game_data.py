import entities
import pygame as pg
import reference_data as ref
import display


class Game():
    """Game class object; contains entities for game and information for PyGame."""
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(ref.screen)
        pg.display.set_caption('Shopkeep')

        self.font = pg.font.Font('display/fonts/UbuntuMono-R.ttf', 26)
        background = pg.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((39, 39, 39))
        self.screen.blit(self.background, (0,0))
        pg.display.flip()
            

    def tick(self):
        """Smallest game time amount passes."""
        #TODO: Capture mouse/keyboard actions
        #TODO: Display screen
        
        for site in entities.sites['object list']:
            site.tick(self)
        entities.player['object'].tick(self)
        entities.shop['object'].tick(self)
