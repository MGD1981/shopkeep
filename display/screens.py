from data import reference_data as ref, entities
import pygame as pg
import sprites


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
        game.screen.blit(self.background, self.position)
        pg.draw.lines(self.surface, 
                      (255, 255, 208),
                      True, 
                      (
                            self.position,
                            self.position[0] + width, self.position[1],
                            self.position[0] + width, self.position[1] + height,
                            self.position[0], self.position[1] + height
                      ),
                      2
        )

    def update(self, game):
        pass


class BannerScreen(Subscreen):

    def __init__(self, width, height):
        super(BannerScreen, self).__init__(width, height)
        self.set_position(0, 0)


class WorldScreen(Subscreen):

    def __init__(self, width, height):
        super(WorldScreen, self).__init__(width, height)
        self.set_position(0, ref.tile_size)

    def initialize_shop_overlay(self, game):
        """Initializes objects on top of background in shopand returns the sprite group"""
        p_x = entities.player['object'].location[0]*ref.tile_size + self.position[0] 
        p_y = entities.player['object'].location[1]*ref.tile_size + self.position[1] 
        print p_x, p_y
        player = sprites.Person(ref.image_path + ref.sprite_dct['player'], p_x, p_y) 
        return pg.sprite.Group((player))

    def update(self, game):
        #draw shop background
        shop = entities.shop['object']
        at_pos = list(self.position)
        tiles = []
        for row in xrange(len(shop.shop_grid)):
            for tile in xrange(len(shop.shop_grid[0])):
                tiles.append(sprites.BackgroundTile(
                    ref.image_path + ref.shop_tile_dct[1]['image file'],
                    at_pos[0], at_pos[1]
                ))
            at_pos[0] += ref.tile_size
            at_pos[1] = self.position[1]
        tiles = pg.sprite.Group(tiles)
        game.screen.blit(game.background, self.position)
        tiles.draw(game.screen)

        #draw shop overlay




class StatusScreen(Subscreen):

    def __init__(self, width, height):
        super(StatusScreen, self).__init__(width, height)
        self.set_position(ref.screen[0]/2 + 1, ref.tile_size)


class MessageScreen(Subscreen):

    def __init__(self, width, height):
        super(MessageScreen, self).__init__(width, height)
        self.set_position(0, ref.tile_size*11)


