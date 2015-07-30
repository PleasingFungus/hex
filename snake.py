''' Main snake game running processes. '''

from area import Area
from cell import CL_FLOOR, CL_STAIR
from mongoose import Mongoose
from player import Player
from point import Point

level_dim = 19

def run_game(main_render, sidebar_render, io):
    ''' The main game loop.
        Params:
            main_render (function<Area>): Render the current game state to the screen.
            sidebar_render (function<Player, Area>): Render metadata to the sidebar.
            io (function<Player, Area>): Query the player for their next action.
    '''
    area = Area(Area.gen_room(level_dim))

    halfwidth = int(level_dim / 2)
    midpoint = Point(halfwidth, halfwidth)
    area.cells[midpoint] = CL_FLOOR()
    player = area.cells[midpoint].actor = Player()

    area.cells[midpoint + Point(2, -1)].actor = Mongoose()

    while True:
        main_render(area)
        sidebar_render(player, area)
        time_taken, should_quit = io(player, area)

        if should_quit:
            break

        if not time_taken:
            continue

        check_stairs(player, area)
        for actor in area.all_actors():
            actor.act(area)

def check_stairs(player, area):
    ''' Check if the player is on the stairs.
        If so, generate a new level.
        Args:
            player (Player): The character controlled by the player.
            area (Area): The current level.
    '''

    loc = area.find_actor(player)
    assert loc != None
    assert loc in area.cells

    cell = area.cells[loc]
    if not cell.is_stairs:
        return

    # on the stairs; new level.
    area.depth += 1
    area.cells = Area.gen_room(level_dim)
    assert loc in area.cells
    area.cells[loc] = CL_FLOOR()
    area.cells[loc].actor = player

    area.cells[Point(loc.x, level_dim-1 - loc.y)] = CL_STAIR() # opposite the player, alternating
