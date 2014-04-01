# coding = utf-8
import sys
import menus
from data import reference_data as ref
import pygame as pg
from pygame.locals import *

#ANSI escape sequence for debug mode:
CSI="\x1B["
# sample: print CSI+"31;40m" + "Colored Text" + CSI + "0m"

class Debug():
    """Class containing functions to display console text for debugging."""

    def cls():
        print CSI+"37;40m" + CSI+"?25l" + CSI+"2J" # clears screen

    def disp_reset():
        print CSI+"0m"

    def default_reset():
        disp_reset()
        print CSI+"?25h" + CSI+"2J"



def run_menu(game, menu):
    """Displays a Menu class object."""
    while True:
        i = 1
        print game.font.get_linesize()
        for option in menu.options:
            text = game.font.render(" %d) %s" % (i, option.text), 1, (255, 255, 208))
            textpos = text.get_rect(left=20, top=game.background.get_width() - (
                             len(menu.options)*(game.font.get_linesize()+26) - ((i-1)*32)))
            game.background.blit(text, textpos)
            game.screen.blit(game.background, (0, 0))
            pg.display.flip()
            i += 1
    
        choice = None
        while choice == None:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    try:
                        choice = int(pg.key.name(event.key))
                        if choice < 1 or choice > len(menu.options):
                            choice = None
                    except:
                        pass

        chosen_option = menu.options[choice - 1]
        if chosen_option.actions != None:
            for action in chosen_option.actions: 
                exec(action)
        if chosen_option.return_value != None:
            return chosen_option.return_value
        return


def draw_map(shopmap):
    cls()
    assert type(shopmap) == list
    for n in xrange(len(shopmap)):
        line = []
        for m in shopmap[n]:
            if m == 0:
                line.append(CSI+"40m" + '  ')
            if m == 't':
                line.append(CSI+"37;40m" + '[]')
            else:
                line.append(CSI+ref.terrain_dct[m][
                        'console representation'])
        line.append(CSI+"40m" + ' ')
        print ''.join(line)
