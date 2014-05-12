from data import reference_data as ref
import pygame as pg


class Subscreen():
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

    def draw(self, game):
        """Draws the entire subscreen to the game screen.
           Takes the game object."""
        width = self.surface.get_width()
        height = self.surface.get_height()
        game.screen.blit(self.background, self.position)
        #Draws border around subscreen:
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


