from data import reference_data as ref, entities
import pygame as pg
import sprites
import copy


class Subscreen(object):
    """Object which holds traits for a particular subscreen of the entire 
    game screen."""

    def __init__(self, width, height):
        self.surface = pg.Surface((width, height))
        self.background = self.surface.convert()
        self.background.fill((39, 39, 39))

    def set_position(self, x_coord, y_coord):
        """Sets the top-left pixel on the game screen where the subscreen will
        be displayed."""
        self.position = (x_coord, y_coord)

    def draw_border(self, game):
        """Draws a border around the entire subscreen to the game screen.
           Takes the game object."""
        width = self.surface.get_width()
        height = self.surface.get_height()
        pg.draw.lines(
                      self.background, 
                      (255, 255, 208),
                      True, 
                      (
                            (0, 0),
                            (width-2, 0),
                            (width-2, height-2),
                            (0, height-2)
                      ),
                      2
        )

    def update(self, game):
        pass


class BannerScreen(Subscreen):

    def __init__(self, width, height):
        super(BannerScreen, self).__init__(width, height)
        self.set_position(0, 0)

    def initialize_sprites(self, game):
        """Initializes buttons for menu and returns the sprite group"""
        buttons = []
        for button in ref.button_dct.keys():
            buttons.append(sprites.Button(
                game,
                ref.image_path + ref.button_dct[button]['image file'],
                ref.button_dct[button]['order'] * ref.tile_size*2, ref.tile_size*1/8
            ))
        self.buttons = pg.sprite.Group(buttons)
        
    def update(self, game):
        self.buttons.draw(self.background)
        if self.surface.get_rect().collidepoint(game.mouse_pos):
            self.buttons.update(game)

        self.draw_border(game)
        game.screen.blit(self.background, self.position)


class WorldScreen(Subscreen):

    def __init__(self, width, height):
        super(WorldScreen, self).__init__(width, height)
        self.set_position(0, ref.tile_size)

    def initialize_sprites(self, game):
        """Initializes objects on top of background in shop and returns the sprite group"""
        #Creates player sprite
        p_x = entities.player['object'].location[0]
        p_y = entities.player['object'].location[1] 
        player = sprites.Person(game, ref.image_path + ref.sprite_dct['player'], p_x, p_y) 
        self.shop_sprites = pg.sprite.Group((player))

        #creates world sprites 
        self.terrain_sprites = pg.sprite.Group()
        at_pos = [0,0]
        tiles = []
        for row in xrange(len(entities.world['grid'])):
            for tile in xrange(len(entities.world['grid'][0])):
                if entities.world['grid'][row][tile] != 't':
                    tiles.append(sprites.BackgroundTile(
                        game,
                        ref.image_path +
                            ref.terrain_dct[entities.world['grid'][
                                                        row][tile]]['image file'],
                        at_pos[0], at_pos[1]
                    ))
                at_pos[0] += entities.world['size']
            at_pos[1] += entities.world['size']
            at_pos[0] = copy.deepcopy(self.position[0])
        self.world_tiles = pg.sprite.Group(tiles) 

        #creates shop_tile sprite group
        shop = entities.shop['object']
        at_pos = [0,0]
        tiles = []
        for row in xrange(len(shop.shop_grid)):
            for tile in xrange(len(shop.shop_grid[0])):
                if entities.shop['object'].shop_grid[row][tile] != 0:
                    tiles.append(sprites.BackgroundTile(
                        game,
                        ref.image_path + 
                            ref.shop_tile_dct[entities.shop['object'].shop_grid[
                                                        row][tile]]['image file'],
                        at_pos[0], at_pos[1]
                    ))
                at_pos[0] += ref.tile_size
            at_pos[1] += ref.tile_size
            at_pos[0] = copy.deepcopy(self.position[0])
        self.shop_tiles = pg.sprite.Group(tiles)


    def update(self, game):

        for action in game.action_log:
            if action == 'refresh background':
                #draw shop background

                self.shop_tiles.draw(self.background)
                self.draw_border(game)
                game.action_log.remove(action)

        #draw shop foreground
        self.shop_sprites.update(game)
        self.shop_sprites.draw(self.background)
        game.screen.blit(self.background, self.position)



class StatusScreen(Subscreen):

    def __init__(self, width, height):
        super(StatusScreen, self).__init__(width, height)
        self.set_position(ref.screen[0]/2 + 1, ref.tile_size)


    def update(self, game):
        self.draw_border(game)
        game.screen.blit(self.background, self.position)

class MessageScreen(Subscreen):

    def __init__(self, width, height):
        super(MessageScreen, self).__init__(width, height)
        self.set_position(0, ref.tile_size*11)

    def update(self, game):
        self.draw_border(game)
        game.screen.blit(self.background, self.position)

