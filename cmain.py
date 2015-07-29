''' The console-based launcher for the game. '''

import logging

from actor import Actor
from area import Area
from cell import CL_FLOOR
from cinput.cimove import go
from crender.crarea import render_area
import curses
from point import Point

def main(scr):
    ''' Run the game. '''
    area = Area(Area.gen_hex_room(20))
    area.cells[Point(11, 10)] = CL_FLOOR()
    player = area.cells[Point(11, 10)].actor = Actor()

    while True:
        render_area(area, scr)
        should_quit = go(player, area)
        if should_quit:
            break

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    curses.wrapper(main)
