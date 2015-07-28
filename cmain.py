''' The console-based launcher for the game. '''

import logging

from area import Area
from crender.crarea import render_area

def main():
    ''' Run the game. '''
    area = Area(Area.gen_room(20))
    render_area(area)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
