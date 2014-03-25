from display import menus, draw_screen
from data import mapper, entities, world_data
import pygame as pg


def start_game():
    pg.init()
    choice = draw_screen.run_menu(menus.StartMenu())
    if choice == "start_new":
        print "Initializing entities..."
        entities.initialize()
        shopmap = mapper.new_map()
        draw_screen.draw_map(entities.world['grid'])
        action = draw_screen.getch()
    if choice == "continue_saved":
        choice = draw_screen.run_menu(menus.ContinueGameMenu())


if __name__ == "__main__":
    start_game()
   
