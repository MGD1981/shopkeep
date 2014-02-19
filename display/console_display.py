# coding = utf-8

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

def draw_map(shopmap):
    cls()
    assert type(shopmap) == list
    for n in range(1,25):
        line = []
        for m in shopmap[n]:
            if m == 0:
                line.append(CSI+"40m" + ' ')
        print ''.join(line)
