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
        self.background.fill(ref.background_color)

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
                      ref.primary_color,
                      True, 
                      (
                            (0, 0),
                            (width-2, 0),
                            (width-2, height-2),
                            (0, height-2)
                      ),
                      1
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
            if ref.button_dct[button]['order'] >= 0:
                buttons.append(sprites.Button(
                    game,
                    button,
                    ref.image_path + ref.button_dct[button]['image file'],
                    ref.button_dct[button]['order'] * ref.tile_size*2, ref.tile_size*1/8
                ))
            else:
                buttons.append(sprites.Button(
                    game,
                    button,
                    ref.image_path + ref.button_dct[button]['image file'],
                    self.surface.get_width() + 
                        (ref.button_dct[button]['order'])* 
                        ref.tile_size*2, 
                    ref.tile_size*1/8 
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

    def initialize_world_sprites(self, game):
        at_pos = [0,0]
        tiles = []
        for row in xrange(entities.world['size']):
            for tile in xrange(entities.world['size']):
                tiles.append(sprites.BackgroundTile(
                    game,
                    ref.image_path +
                        ref.terrain_dct[entities.world['grid'][
                                                    row][tile]]['image file'],
                    at_pos[0], at_pos[1]
                ))
                at_pos[0] +=  self.surface.get_width()/entities.world['size']
            at_pos[1] += self.surface.get_width()/entities.world['size']
            at_pos[0] = copy.deepcopy(self.position[0])
        self.world_tiles = pg.sprite.Group(tiles) 
    
    def initialize_site_sprites(self, game):
        tiles = []
        for site in entities.sites['object list']:
            tiles.append(sprites.BackgroundTile(
                game,
                ref.image_path +
                    ref.structure_type_dct[site.structure]['image file'],
                site.location[0], site.location[1]
            ))
        self.site_tiles = pg.sprite.Group(tiles)

    def initialize_sprites(self, game):
        """Initializes objects on top of background and returns the sprite group"""
        #Creates player sprite
        p_x = entities.player['object'].location[0]
        p_y = entities.player['object'].location[1] 
        player = sprites.Person(game, ref.image_path + ref.sprite_dct['player'], p_x, p_y) 
        self.shop_sprites = pg.sprite.Group((player))

        self.initialize_world_sprites(game)
        self.initialize_site_sprites(game)

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

        if game.view == 'shop':
            if 'reinitialize shop' in game.action_log:
                self.background.fill(ref.background_color)
                game.action_log.remove('reinitialize shop')
                game.action_log.append('refresh background')
            for action in game.action_log:
                if action == 'refresh background':
                        #draw shop background

                        self.shop_tiles.draw(self.background)
                        self.draw_border(game)
                        game.action_log.remove(action)

                #draw shop foreground
            self.shop_sprites.update(game)
            self.shop_sprites.draw(self.background)

        elif game.view == 'world':
            for action in game.action_log:
                if action == 'refresh background':
                    self.background.fill(ref.background_color)
                    self.initialize_world_sprites(game)
                    self.world_tiles.draw(self.background)
                    self.site_tiles.draw(self.background)
                    game.action_log.remove(action)

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

