''' The console-based launcher for the game. '''

import logging

from actor import Actor
from area import Area
from cell import CL_FLOOR
from crender.crarea import render_area
from point import Point

def main():
    ''' Run the game. '''
    area = Area(Area.gen_room(20))
    area.cells[Point(10, 10)] = CL_FLOOR()
    area.cells[Point(10, 10)].actor = Actor()
    render_area(area)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
