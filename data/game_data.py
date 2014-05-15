import entities
import pygame as pg
from pygame.locals import *
import reference_data as ref
import display
from display import screens, draw_screen, menus


class Game():
    """Game class object; contains entities for game and information for PyGame."""
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(ref.screen)
        pg.display.set_caption('Shopkeep')

        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        self.menu_font = pg.font.Font('display/fonts/UbuntuMono-R.ttf', ref.tile_size * 26/32)
        self.info_font = pg.font.Font('display/fonts/UbuntuMono-R.ttf', ref.tile_size * 11/32)

        self.action_log = ['refresh background']

        self.screens = {
            'banner': screens.BannerScreen(ref.screen[0], ref.screen[1]/16),
            'world': screens.WorldScreen(ref.screen[0]/2, ref.screen[1]*10/16),
            'status': screens.StatusScreen(ref.screen[0]/2, ref.screen[1]*10/16),
            'message': screens.MessageScreen(ref.screen[0], ref.screen[1]*5/16)
        }


        background = pg.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(ref.background_color)
        self.screen.blit(self.background, (0,0))
        pg.display.flip()


    def tick(self):
        """Smallest game time amount passes."""
        
        self.mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                if self.keys[K_ESCAPE]:
                    draw_screen.run_menu(self, menus.StartMenu())

                #DevMode (Ctrl-Shift-D)
                if (
                    self.keys[K_d] and 
                    (self.keys[K_RCTRL] or self.keys[K_LCTRL]) and
                    (self.keys[K_RSHIFT] or self.keys[K_LSHIFT])
                ):
                    import traceback
                    while True:
                        command = str(raw_input('>> '))
                        if command == 'exit':
                            break
                        try:
                            exec(command)
                        except Exception as e:
                            tb = traceback.format_exc()
                            print tb
                            print "Please try again, or type 'exit' to exit."

            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
        for site in entities.sites['object list']:
            site.tick()
        #entities.shop['object'].tick(self)

        for screen in self.screens.keys():
            self.screens[screen].update(self)
        pg.display.flip()
        print "FPS: %d" % self.clock.get_fps()
