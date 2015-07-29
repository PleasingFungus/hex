''' The console-based launcher for the game. '''

import logging

from cinput.cimove import go
from crender.crarea import render_area, render_sidebar
import curses
from snake import run_game

def main(scr):
    ''' Run the game. '''
    curses.curs_set(0)

    sidebar_width = 12
    main_width = curses.COLS - sidebar_width
    sidebar_window = curses.newwin(curses.LINES, sidebar_width, 0, 0)
    main_window = curses.newwin(curses.LINES, main_width, 0, sidebar_width) 

    def render(area):
        ''' Render info about the current area to the entire console. '''
        render_area(area, main_window)
        render_sidebar(area, sidebar_window)
        # FIXME: this displays black until prompted for input (???)
    io = lambda player,area: go(scr.getkey(), player, area)
    run_game(render, io)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    curses.wrapper(main)
