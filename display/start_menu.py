from console_display import *

def init():

    cls()
    print "1) Start New Game"
    print "2) Continue Saved Game"
    print "3) Quit"
    
    try:
        choice = int(getch())
    except:
        init()
    if choice == 1:
        start_new()
    elif choice == 2:
        continue_saved()
    elif choice == 3:
        disp_reset()
    else:
        init()
