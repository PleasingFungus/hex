''' The console-based launcher for the game. '''

import logging

from area import Area
from cell import CL_FLOOR
from cinput.cimove import go
from crender.crarea import render_area
import curses
from player import Player
from point import Point

def main(scr):
    ''' Run the game. '''
    curses.curs_set(0)

    area = Area(Area.gen_room(20))
    area.cells[Point(10, 10)] = CL_FLOOR()
    player = area.cells[Point(10, 10)].actor = Player()

    while True:
        render_area(area, scr)
        command = scr.getkey()
        should_quit = go(command, player, area)
        if should_quit:
            break

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    curses.wrapper(main)
