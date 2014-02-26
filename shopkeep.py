from display import menus, console_display
from data import mapper, entities
from display.menus import *

def start_game():
    choice = run_menu(StartMenu())
    if choice == "start_new":
        entities.initialize()
        shopmap = mapper.new_map()
        console_display.draw_map(shopmap)
        action = console_display.getch()
        print entities.weapons
    if choice == "continue_saved":
        choice = run_menu(ContinueGameMenu())


if __name__ == "__main__":
    start_game()
   
