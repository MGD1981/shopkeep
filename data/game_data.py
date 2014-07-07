import time
import entities
import pygame as pg
from pygame.locals import *
import reference_data as ref
import display
from display import screens, draw_screen, menus
from copy import copy


class Game():
    """Game class object; contains entities for game and information for PyGame."""
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(ref.screen)
        pg.display.set_caption('Shopkeep')

        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        self.menu_font = pg.font.Font('display/fonts/UbuntuMono-R.ttf', int(ref.scale*26))
        self.info_font = pg.font.Font('display/fonts/UbuntuMono-R.ttf', int(ref.scale*11))

        self.action_log = GameLog(['refresh background'])
        self.speed = 'normal'
        pg.time.set_timer(pg.USEREVENT, ref.game_speed_dct[self.speed]) #game ticks
        pg.time.set_timer(pg.USEREVENT+1, ref.game_speed_dct[self.speed]/2) #sprite animation ticks
        self.blink = False

        self.speed_keys = [K_1, K_2, K_3, K_4]

        self.screens = {
            'banner': screens.BannerScreen(ref.screen[0], ref.screen[1]/16),
            'world': screens.WorldScreen(ref.screen[0]/2, ref.screen[1]*10/16),
            'status': screens.StatusScreen(ref.screen[0]/2, ref.screen[1]*10/16),
            'message': screens.MessageScreen(ref.screen[0], ref.screen[1]*5/16)
        }

        self.message_log = MessageLog(
            [],
            max_length=self.screens['message'].background.get_height() / self.info_font.get_linesize() - 1
        )

        background = pg.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(ref.background_color)
        self.screen.blit(self.background, (0,0))
        pg.display.flip()


    def pause(self):
        """Pauses timed events."""
        pg.time.set_timer(pg.USEREVENT, 0)

    def unpause(self):
        """Unpauses timed events."""
        pg.time.set_timer(pg.USEREVENT, ref.game_speed_dct[self.speed])


    def tick(self):
        """Smallest game time amount passes."""

        self.mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                if self.keys[K_ESCAPE]:
                    draw_screen.run_menu(self, menus.StartMenu('in_progress'))
                if self.keys[K_w]:
                    self.action_log += 'w'
                    self.action_log.append('refresh background')
                if self.keys[K_s]:
                    self.action_log.append('shop view')
                    self.action_log.append('refresh background')
                if self.keys[K_TAB]:
                    self.action_log.append('switch info view')

                if self.keys[K_LCTRL] or self.keys[K_RCTRL]:
                    if self.keys[K_1]:
                        self.speed = 'normal'
                        self.action_log.append('speed change')
                    if self.keys[K_2]:
                        self.speed = 'fast'
                        self.action_log.append('speed change')
                    if self.keys[K_3]:
                        self.speed = 'ultra'
                        self.action_log.append('speed change')
                    if self.keys[K_4]:
                        self.speed = 'ludicrous'
                        self.action_log.append('speed change')
                if 'speed change' in self.action_log:
                    pg.time.set_timer(pg.USEREVENT, ref.game_speed_dct[self.speed])
                    self.action_log.remove('speed change')

                #TODO: Remove this -- for testing only
                if self.keys[K_h]:
                    import hero_data
                    import item_data
                    hero_data.Hero().generate('town').inventory.append(item_data.Weapon().generate())
                    
                if self.keys[K_t]:
                    for site in entities.sites['object list']:
                        site.structure.transform()
                        self.action_log.append('transformation')
                if self.keys[K_m]:
                    print entities.heroes['object list'][0].perceptions.economy
                if self.keys[K_i]:
                    import item_data
                    for hero in entities.heroes['object list']:
                        hero.inventory.append(item_data.Weapon().generate())
                if self.keys[K_e]:
                    print entities.town['object'].economy.material_value_table


                #DevMode (Ctrl-Shift-D)
                if (
                    self.keys[K_d] and 
                    (self.keys[K_RCTRL] or self.keys[K_LCTRL]) and
                    (self.keys[K_RSHIFT] or self.keys[K_LSHIFT])
                ):
                    self.pause()
                    import traceback
                    while True:
                        command = str(raw_input('>> '))
                        if command == 'exit':
                            self.unpause()
                            break
                        try:
                            exec(command)
                        except Exception as e:
                            tb = traceback.format_exc()
                            print tb
                            print "Please try again, or type 'exit' to exit."

            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            if event.type == pg.USEREVENT:
                for site in entities.sites['object list']:
                    site.tick(self)
                for hero in entities.heroes['object list']:
                    hero.tick(self)
                entities.player['object'].tick(self)
            if event.type == pg.USEREVENT+1:
                self.blink = not self.blink

        #entities.shop['object'].tick(self)
        entities.town['object'].tick(self)
        
        #update graphics
        for screen in self.screens.keys():
            self.screens[screen].update(self)
        pg.display.flip()
        #NOTE: For dev:
        #print "FPS: %d" % self.clock.get_fps()


class GameLog():
    """Messaging system for functions to check.
       Every frame, back log switches to front, and back is reinitialized.
       Messages are placed in the backlog, and actions check the frontlog.
       Actions are therefore always one tick (frame) behind.
    """
    def __init__(self, starting_action_list=None):
        self.frontlog = []
        self.backlog = []
        if starting_action_list != None:
            self.frontlog.extend(starting_action_list)

    def post_message(self, message):
        self.backlog.append(message)

    def get_messages(self):
        return self.frontlog

    def clear_messages(self):
        self.frontlog = copy.deepycopy(self.backlog)
        self.backlog = []

    def __iadd__(self, message): #same as post_message()
        self.backlog.append(message)

    def __iter__(self):
        self.length = len(self.frontlog)
        self.current_index = 0
        return self

    def next(self):
        if self.current_index == self.length:
            raise StopIteration
        current = self.frontlog[self.current_index]
        self.current_index += 1
        return current
        

class MessageLog(list):
    
    def __init__(self, *args, **kwargs):
        self.max_length = 20
        super(MessageLog, self).__init__(args[0])
        if 'max_length' in kwargs.keys():
            self.max_length = kwargs['max_length']
        

    def __iadd__(self, other):
        if type(other) == str:
            other = [other]
        if len(self) == 0:
            self = MessageLog(other[:self.max_length], max_length=self.max_length)
        else:
            other.extend(self)
            self = MessageLog(other[:self.max_length], max_length=self.max_length)
        return self

