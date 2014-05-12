from display import menus, draw_screen
from data import mapper, entities, world_data, reference_data as ref, game_data
import pygame as pg


def start_game():
    game = game_data.Game()
    clock = pg.time.Clock()
    draw_screen.run_menu(game, menus.StartMenu())

    while True:
        game.clock.tick()
        game.tick()


if __name__ == "__main__":
    start_game()
   
