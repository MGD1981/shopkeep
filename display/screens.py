from data import reference_data as ref, entities
import pygame as pg
import sprites
import copy
import operator


def clear_callback(surface, rect):
    surface.fill(ref.background_color, rect)

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
        self.view = 'shop'
        self.mouse_over = None


    def initialize_hero_sprites(self, game):
        tile_scale = self.surface.get_width()/entities.world['size']
        tiles = []
        for hero in [x for x in entities.heroes['object list'] if x.traveling]:
            tiles.append(sprites.BackgroundTile(
                game,
                ref.image_path + ref.hero_dct['image file'],
                hero.location[0]*tile_scale, 
                hero.location[1]*tile_scale
            ))
        self.hero_tiles = pg.sprite.Group(tiles)

    def initialize_refreshed_world_sprites(self, game):
        tile_scale = self.surface.get_width()/entities.world['size']
        tiles = []
        site_locs = [s.location for s in entities.sites['object list']]
        for hero_tile in self.hero_tiles:
            hero_loc = [x/tile_scale for x in hero_tile.rect[0:2]] 
            if hero_loc in site_locs:
                site = [s for s in entities.sites['object list'] if s.location == hero_loc][0]
                tiles.append(sprites.BackgroundTile(
                    game,
                    ref.image_path +
                        site.structure.get_attribute('image file'),
                    hero_tile.rect[0],
                    hero_tile.rect[1]
                ))
            else:
                tiles.append(sprites.BackgroundTile(
                    game,
                    ref.image_path +
                        ref.terrain_dct[entities.world['grid'][
                            hero_tile.rect[1]/tile_scale][
                            hero_tile.rect[0]/tile_scale]]['image file'],
                        hero_tile.rect[0],
                        hero_tile.rect[1]
                ))
        self.refreshed_world_sprites = pg.sprite.Group(tiles)

    def initialize_world_sprites(self, game):
        tile_scale = self.surface.get_width()/entities.world['size']
        site_locs = [site.location for site in entities.sites['object list']]
        at_pos = [0,0]
        tiles = []
        for row in xrange(entities.world['size']):
            for tile in xrange(entities.world['size']):
                if [at_pos[0]/tile_scale, at_pos[1]/tile_scale] not in site_locs:
                    tiles.append(sprites.BackgroundTile(
                        game,
                        ref.image_path +
                            ref.terrain_dct[entities.world['grid'][
                                                        row][tile]]['image file'],
                        at_pos[0], at_pos[1]
                    ))
                at_pos[0] += tile_scale
            at_pos[1] += tile_scale
            at_pos[0] = copy.deepcopy(self.position[0])
        self.world_tiles = pg.sprite.Group(tiles) 
    
    def initialize_site_sprites(self, game):
        tiles = []
        for site in entities.sites['object list']:
            tiles.append(sprites.BackgroundTile(
                game,
                ref.image_path +
                    site.structure.get_attribute('image file'),
                site.location[0]*(self.surface.get_width()/entities.world['size']),
                site.location[1]*(self.surface.get_width()/entities.world['size'])
            ))
        self.site_tiles = pg.sprite.Group(tiles)

    def initialize_shop_sprites(self, game):
        #Creates player and shopper sprites
        p_x = entities.player['object'].location[0]
        p_y = entities.player['object'].location[1] 
        shop_sprites = []
        shop_sprites.append(sprites.Player(game, ref.sprite_dct['player'], p_x, p_y))
        for hero in [h for h in entities.heroes['object list'] if h.shop_location != None]:
            shop_sprites.append(sprites.Hero(
                hero.hero_id, game, ref.sprite_dct['hero'], hero.shop_location[0], hero.shop_location[1]
            ))
        self.shop_sprites = pg.sprite.Group(shop_sprites)


    def initialize_sprites(self, game):
        """Initializes objects on top of background and returns the sprite group"""
        
        self.initialize_shop_sprites(game)
        self.initialize_world_sprites(game)
        self.initialize_site_sprites(game)
        self.initialize_hero_sprites(game)

        #creates shop_tile sprite groups
        shop = entities.shop['object']
        at_pos = [0,0]
        background_tiles = []
        impassable_tiles = []
        for row in xrange(len(shop.shop_grid)):
            for tile in xrange(len(shop.shop_grid[0])):
                if shop.shop_grid[row][tile] != 0:
                    if ref.shop_tile_dct[shop.shop_grid[row][tile]]['passable']:
                        tile_group = background_tiles
                    else:
                        tile_group = impassable_tiles
                    tile_group.append(sprites.BackgroundTile(
                        game,
                        ref.image_path + 
                            ref.shop_tile_dct[shop.shop_grid[
                                                        row][tile]]['image file'],
                        at_pos[0], at_pos[1]
                    ))
                at_pos[0] += ref.tile_size
            at_pos[1] += ref.tile_size
            at_pos[0] = copy.deepcopy(self.position[0])
        self.background_shop_tiles = pg.sprite.Group(background_tiles)
        self.impassable_shop_tiles = pg.sprite.Group(impassable_tiles)


    def update(self, game):
        try:
            self.mouse_over = [
                sprite for sprite in self.site_tiles if 
                sprite.rect.collidepoint(map(operator.sub, pg.mouse.get_pos(), self.position))][0
            ]
        except IndexError:
            self.mouse_over = None
            
        if 'world view' in game.action_log:
            self.view = 'world'
            game.action_log.remove('world view')
        if 'shop view' in game.action_log:
            self.view = 'shop'
            game.action_log.remove('shop view')
        if self.view == 'shop':
            for action in game.action_log:
                if action == 'refresh background':
                        #draw shop background
                        self.background.fill(ref.background_color)
                        self.background_shop_tiles.draw(self.background)
                        self.impassable_shop_tiles.draw(self.background)
                        game.action_log.remove(action)

            #draw shop foreground
            shop_sprite_list = pg.sprite.LayeredUpdates(self.shop_sprites).sprites()
            shop_sprite_list.sort(key=lambda x: x.rect.bottom)
            self.shop_sprites = pg.sprite.LayeredUpdates(shop_sprite_list)
            self.shop_sprites.update(game)
            self.shop_sprites.draw(self.background)

        elif self.view == 'world':
            for action in game.action_log:
                if action in ['refresh background', 'transformation']: #TODO: transformations shouldn't need full refresh
                    self.background.fill(ref.background_color)
                    self.initialize_world_sprites(game)
                    self.initialize_site_sprites(game) 
                    self.world_tiles.draw(self.background)
                    self.site_tiles.draw(self.background)
                    game.action_log.remove(action)
            self.hero_tiles.clear(self.background, clear_callback)
            self.initialize_refreshed_world_sprites(game)
            self.refreshed_world_sprites.draw(self.background)
            self.initialize_hero_sprites(game)
            self.hero_tiles.draw(self.background)

        game.screen.blit(self.background, self.position)

class StatusScreen(Subscreen):

    def __init__(self, width, height):
        super(StatusScreen, self).__init__(width, height)
        self.set_position(ref.screen[0]/2 + 1, ref.tile_size)
        self.view = 'town info'

    def get_shop_info(self):
        info_list = [
            '--Shop Resources--',
            '',
            'coins:'
        ]
        for coin in sorted(entities.player['object'].coins.keys()):
            info_list.append('  %s: %d' % (
                coin,
                entities.player['object'].coins[coin]
            ))
        info_list.append('')
        for resource_type in sorted(entities.shop['object'].resources.keys()):
            info_list.append('%s:' % resource_type)
            for resource in sorted(entities.shop['object'].resources[resource_type]):
                info_list.append('  %s: %d kg' % (
                    resource, 
                    entities.shop['object'].resources[resource_type][resource]/1000
            ))
            info_list.append('')
        return info_list

    def get_world_info(self):
        info_list = [
            '--Site Information--',
            ''
        ]
        for site in sorted(entities.sites['object list']):
            if site.structure.get_attribute('site type') == 'resource':
                info_list.extend([
                    '%s at %r:' % (site.structure.structure_type, site.location),
                    '  %d / %d workers on site.' % (
                        site.structure.workers, 
                        site.structure.get_attribute('worker capacity')
                        ),
                    '  %s remaining: %d kg' % (site.resource, site.harvestable/1000),
                    '  %d seconds until next harvest.' % site.structure.time_until_harvest
                ])
            elif site.structure.get_attribute('site type') == 'adventure':
                heroes = ''
                monsters = ''
                for hero_id in site.structure.workers:
                    heroes += '%s, ' % [
                        x.name for x in entities.heroes['object list'
                        ] if x.hero_id == hero_id][0
                        ]
                if len(heroes) > 2:
                    heroes = heroes[:-2]
                else:
                    heroes = 'None'
                for monster_id in site.structure.monsters:
                    monsters += '%s, ' % [
                        x.name for x in entities.monsters['object list'
                        ] if x.monster_id == monster_id][0
                        ]
                if len(monsters) > 2:
                    monsters = monsters[:-2]
                else:
                    monsters = 'None'

                info_list.extend([
                    '%s at %r:' % (site.structure.structure_type, site.location),
                    '  heroes on site: %s' % heroes,
                    '  monsters remaining: %s' % monsters
                ])

        return info_list

    def get_town_info(self):
        info_list = [
            '--Town Information--',
            '',
            'population: %d' % entities.town['object'].population
        ]
        for occupation in sorted(entities.town['object'].occupations.keys()):
            info_list.append(
                '  ' + occupation + (': %d' % entities.town['object'].occupations[occupation])
            )
        info_list.append('')
        for resource_type in sorted(entities.town['object'].resources.keys()):
            info_list.append('%s:' % resource_type)
            for resource in sorted(entities.town['object'].resources[resource_type]):
                info_list.append('  %s: %d kg' % (
                    resource, 
                    entities.town['object'].resources[resource_type][resource]['available']/1000
                ))
            info_list.append('')
        return info_list


    def update(self, game):
        if 'switch info view' in game.action_log:
            try:
                self.view = [
                    x for x in ref.button_dct.keys() if ref.button_dct[x][
                    'order'] == ref.button_dct[self.view]['order'] - 1
                ][0]
            except IndexError:
                self.view = [
                    x for x in ref.button_dct.keys() if ref.button_dct[x][
                    'order'] == -1
                ][0]
            game.action_log.remove('switch info view')
        if 'town info view' in game.action_log:
            self.view = 'town info'
            game.action_log.remove('town info view')
        if 'world info view' in game.action_log:
            self.view = 'world info'
            game.action_log.remove('world info view')
        if 'shop info view' in game.action_log:
            self.view = 'shop info'
            game.action_log.remove('shop info view')

        if self.view == 'town info':
            info_list = self.get_town_info() 
        if self.view == 'world info':
            info_list = self.get_world_info()
        if self.view == 'shop info':
            info_list = self.get_shop_info()

        self.background.fill(ref.background_color)
        i = 0
        for info in info_list:
            text = game.info_font.render("%s" % (info), 0, ref.primary_color)
            if 20+(i+2)*game.info_font.get_linesize() < self.background.get_height():
                textpos = text.get_rect(
                    left=20, 
                    top=(20+i*game.info_font.get_linesize())
                )
            else:
                textpos = text.get_rect(
                    left=20+self.background.get_width()/2, 
                    top=(20+(i+4)*game.info_font.get_linesize() - self.background.get_height())
                )
            self.background.blit(text, textpos)
            i += 1

        self.draw_border(game)
        game.screen.blit(self.background, self.position)

class MessageScreen(Subscreen):

    def __init__(self, width, height):
        super(MessageScreen, self).__init__(width, height)
        self.set_position(0, ref.tile_size*11)
        self.rollover_mode = True

    def update(self, game):
        info_list = []
        if self.rollover_mode and game.screens['world'].view == 'world':
            world_screen = game.screens['world']
            if world_screen.mouse_over != None:
                for site in [
                    s for s in entities.sites['object list'] if s.location == map(
                    lambda x: x/world_screen.mouse_over.rect[2], world_screen.mouse_over.rect[:2])
                ]:
                    if site.structure.get_attribute('site type') == 'resource':
                        info_list.append(
                            "%s %s" % (site.resource.capitalize(), site.structure.structure_type)
                        )
                    else:
                        info_list.append(
                            "%s" % (site.structure.structure_type.capitalize())
                        )
        if not self.rollover_mode or len(info_list) == 0:
            info_list = game.message_log

        self.background.fill(ref.background_color)
        i = 0
        for info in info_list:
            text = game.info_font.render("%s" % (info), 0, ref.primary_color)
            if 20+(i+2)*game.info_font.get_linesize() < self.background.get_height():
                textpos = text.get_rect(
                    left=20, 
                    top=(20+i*game.info_font.get_linesize())
                )
            else:
                textpos = text.get_rect(
                    left=20+self.background.get_width()/2, 
                    top=(20+i*game.info_font.get_linesize() - self.background.get_height())
                )
            self.background.blit(text, textpos)
            i += 1
        self.draw_border(game)
        game.screen.blit(self.background, self.position)


