''' The console-based launcher for the game. '''

import logging

from cinput.cimove import go
from crender.crarea import render_area
import curses
from snake import run_game

def main(scr):
    ''' Run the game. '''
    curses.curs_set(0)

    renderer = lambda area: render_area(area, scr)
    io = lambda player,area: go(scr.getkey(), player, area)
    run_game(renderer, io)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    curses.wrapper(main)
