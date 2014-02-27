from display import menus, draw_screen
from data import mapper, entities
from display.menus import *

def start_game():
    choice = draw_screen.run_menu(StartMenu())
    if choice == "start_new":
        entities.initialize()
        shopmap = mapper.new_map()
        draw_screen.draw_map(shopmap)
        action = draw_screen.getch()
        print entities.weapons
    if choice == "continue_saved":
        choice = run_menu(ContinueGameMenu())


if __name__ == "__main__":
    start_game()
   
