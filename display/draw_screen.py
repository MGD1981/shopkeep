# coding = utf-8
import sys
import menus
import data
import sprites
from data import reference_data as ref
import pygame as pg
from pygame.locals import *
import copy

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


def draw_shop_background(game, height, width, image):
    """Renders the entire shop background (floor) to the screen"""
    position = copy.deepcopy(ref.shop_position)
    tiles = []
    for row in xrange(height):
        for tile in xrange(width):
            tiles.append(sprites.BackgroundTile(image, position[0], position[1]))
            position[1] += ref.tile_size
        position[0] += ref.tile_size
        position[1] = ref.shop_position[1]
    tiles = pg.sprite.Group(tiles)
    game.screen.blit(game.background, (0, 0))
    tiles.draw(game.screen)


def update_shop_background(game, topleft, bottomright, image):
    position = copy.deepcopy(ref.shop_position)
    position[0] = topleft[0]
    position[1] = topleft[1]
    horiz = bottomright[0] - topleft[0]
    vert = topleft[1] - bottomright[1]
    tiles = []
    for row in xrange(vert):
        for tile in xrange(horiz):
            tiles.append(sprites.BackgroundTile(image, position[0], position[1]))
            position[1] += ref.tile_size
        position[0] += ref.tile_size
        position[1] = topleft[1]
    tiles = pg.sprite.Group(tiles)
    game.screen.blit(data.entities.shop['object'].surface, ref.shop_position)
    tiles.draw(game.screen)


def initialize_shop_overlay(game):
    """Initializes objects on top of background in shop"""
    shop_pos = copy.deepcopy(ref.shop_position)
    p_x = data.entities.player['object'].location[0] + shop_pos[0] 
    p_y = data.entities.player['object'].location[1] + shop_pos[1] 
    player = sprites.Person(ref.image_path + ref.sprite_dct['player'], p_x, p_y) 
    game.overlay = pg.sprite.Group((player))


def draw_shop_overlay(game):
    """Draws objects on top of background in shop"""
    game.overlay.update(game)
    #game.screen.blit(data.entities.shop['object'].surface, ref.shop_position)
    game.overlay.draw(game.screen)
    pg.display.flip()
    


def run_menu(game, menu):
    """Displays a Menu class object."""
    while True:
        i = 1
        for option in menu.options:
            text = game.font.render(" %d) %s" % (i, option.text), 1, (255, 255, 208))
            textpos = text.get_rect(left=20, bottom=game.background.get_height() - (
                             len(menu.options)*(game.font.get_linesize()) - ((i-1)*ref.tile_size)))
            game.background.blit(text, textpos)
            game.screen.blit(game.background, (0, 0))
            i += 1
        pg.display.flip()
    
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


def draw_map(shopmap, debug=False):
    if debug:
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
