import entities
import pygame as pg
import reference_data as ref
import display
from display import screens


class Game():
    """Game class object; contains entities for game and information for PyGame."""
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(ref.screen)
        pg.display.set_caption('Shopkeep')

        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        self.font = pg.font.Font('display/fonts/UbuntuMono-R.ttf', ref.tile_size * 26/32)

        self.screens = {
            'banner': screens.BannerScreen(ref.screen[0], ref.screen[1]/16),
            'world': screens.WorldScreen(ref.screen[0]/2, ref.screen[1]*10/16),
            'status': screens.StatusScreen(ref.screen[0]/2, ref.screen[1]*10/16),
            'message': screens.MessageScreen(ref.screen[0], ref.screen[1]*5/16)
        }

        background = pg.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((39, 39, 39))
        self.screen.blit(self.background, (0,0))
        pg.display.flip()


    def tick(self):
        """Smallest game time amount passes."""
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
        for site in entities.sites['object list']:
            site.tick(self)
        #entities.shop['object'].tick(self)
        for screen in self.screens.keys():
            self.screens[screen].update(self)
        display.draw_screen.draw_shop_overlay(self)
        pg.display.flip()
        print self.clock.get_fps()
