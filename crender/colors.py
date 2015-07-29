''' Setup color for a screen. '''

import curses

# TODO: add an abstraction layer for bold/bright colors

COL_WHITE, COL_BLACK, COL_BLUE, COL_CYAN, COL_GREEN, COL_MAGENTA, COL_RED, COL_YELLOW, NUM_COLORS = range(9)
colors = [curses.COLOR_WHITE, curses.COLOR_BLACK, curses.COLOR_BLUE, curses.COLOR_CYAN,
          curses.COLOR_GREEN, curses.COLOR_MAGENTA, curses.COLOR_RED, curses.COLOR_YELLOW]

def init_colors():
    for i in range(1, NUM_COLORS): # skip white
        curses.init_pair(i, colors[i], curses.COLOR_BLACK)
