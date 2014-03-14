# coding = utf-8
import menus

CSI="\x1B["
# sample: print CSI+"31;40m" + "Colored Text" + CSI + "0m"

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()

def cls():
    print CSI+"37;40m" + CSI+"?25l" + CSI+"2J" # clears screen

def disp_reset():
    print CSI+"0m"

def default_reset():
    disp_reset()
    print CSI+"?25h" + CSI+"2J"



def run_menu(menu):
    """Displays a Menu class object."""

    print 24*'\n'
    cls()
    i = 1
    for option in menu.options:
        print " %d) %s" % (i, option.text)
        i += 1
    print '\n\n'

    try:
        choice = int(getch())
        chosen_option = menu.options[choice - 1]
    except:
        return run_menu(menu)
    if chosen_option.actions != None:
        for action in chosen_option.actions: 
            exec(action)
    if chosen_option.return_value != None:
        return chosen_option.return_value
    return


def draw_map(shopmap):
    cls()
    assert type(shopmap) == list
    for n in range(1,25):
        line = []
        for m in shopmap[n]:
            if m == 0:
                line.append(CSI+"40m" + ' ')
            if m == 'g':
                line.append(CSI+"42m" + ' ')
            if m == 'w':
                line.append(CSI+"46m" + ' ')
            if m == 'r':
                line.append(CSI+"43m" + ' ')
        line.append(CSI+"40m" + ' ')
        print ''.join(line)
