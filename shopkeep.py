from display import menus, console_display
from data import mapper
from display.menus import *

def start_game():
    choice = run_menu(StartMenu())
    if choice == "start_new":
        shopmap = mapper.new_map()
        console_display.draw_map(shopmap)
        action = console_display.getch()
    if choice == "continue_saved":
        pass


if __name__ == "__main__":
    start_game()
   
