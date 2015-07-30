''' Main snake game running processes. '''

from area import Area
from astar import a_star_search
from cell import CL_FLOOR, CL_STAIR
from mongoose import Mongoose
from player import Player
from point import Point
from random import choice

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
    add_enemies(player, area)

    while True:
        main_render(area)
        sidebar_render(player, area)
        time_taken = io(player, area)

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

    add_enemies(player, area)

def add_enemies(player, area):
    ''' Generate enemies and place them on the level.
        Args:
            player (Player): The character controlled by the player.
            area (Area): The current level.
    '''
    player_loc = area.find_actor(player)
    assert player_loc != None
    assert player_loc in area.cells

    # spawn 1 mongoose per depth
    for i in range(area.depth):
        for i in range(10000): # eventually bail

            # repeatedly choose random cells
            loc, cell = choice(list(area.cells.items()))
            # discard ones that already have terrain or other actors
            if cell.is_full():
                continue
            # also discard those which can't get to the player, or which are too close
            to_player = a_star_search(area.cells, loc, player_loc)
            if not to_player or len(to_player) < 4:
                continue

            # actually place an enemy
            cell.actor = Mongoose()
            break

