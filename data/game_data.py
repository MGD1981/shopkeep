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

        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        self.font = pg.font.Font('display/fonts/UbuntuMono-R.ttf', ref.tile_size * 26/32)
        background = pg.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((39, 39, 39))
        self.screen.blit(self.background, (0,0))
        pg.display.flip()
        self.overlay = None

    def initialize_overlay(self):
        display.draw_screen.initialize_shop_overlay(self)


    def tick(self):
        """Smallest game time amount passes."""
        #TODO: Capture mouse/keyboard actions
        #TODO: Display screen
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
        for site in entities.sites['object list']:
            site.tick(self)
        entities.shop['object'].tick(self)
        display.draw_screen.draw_shop_overlay(self)
