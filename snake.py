''' Main snake game running processes. '''

from area import Area
from cell import CL_FLOOR
from player import Player
from point import Point

def run_game(render, io):
    ''' The main game loop.
        Params:
            render (function<Area>): Render the current game state to the screen.
            io (function<Player, Area>): Query the player for their next action.
    '''
    area = Area(Area.gen_room(20))
    area.cells[Point(10, 10)] = CL_FLOOR()
    player = area.cells[Point(10, 10)].actor = Player()

    while True:
        render(area)
        should_quit = io(player, area)
        if should_quit:
            break

