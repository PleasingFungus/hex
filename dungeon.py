''' Functions for generating levels. '''

from astar import a_star_search
from cell import CL_FLOOR, CL_WALL, CL_STAIR
from ghost import Ghost
from mongoose import Mongoose
from point import Point
from rand import random_choose_weighted, choice

def new_level(player, player_loc, depth, dim):
    ''' Generate a new level.
    Args:
        player <Player>: The actor controlled by the player.
        loc <Point>: The location of the player on the last level. (Assumption: dim is constant?)
        depth <int>: The number of the floor, starting from 1.
        dim <int>: The number of rows & columns to generate.
    Returns:
        map<Point, Cell>: A map from locations to the cells therein.
    '''

    for i in range(100):
        # generate terrain
        cells = gen_room(dim)

        # place the player
        assert player_loc in cells
        cells[player_loc] = CL_FLOOR()
        cells[player_loc].actor = player

        # place the stairs out
        stairs_loc = Point(int(dim/2), 1 if depth % 2 else dim - 2) # opposite the player, alternating
        cells[stairs_loc] = CL_STAIR()
        
        # place enemies
        add_enemies(player, player_loc, cells, depth)

        # sanity check
        path = a_star_search(cells, player_loc, stairs_loc, lambda cell: not cell.solid)
        if path:
            return cells
        # otherwise, generate a new level
        # TODO: would be nice to log this somehow

    raise RuntimeError("Couldn't generate a valid level!")

def gen_room(dim):
    ''' Generate a largely hollow room of the given dimensions, starting from the origin.
    
    Args:
        dim (int): The number of rows & columns to generate.
    Returns:
        dict<Point, Cell>: A set of cells completely filling the given dimensions.
    '''
    cells = {}
    for x in range(dim):
        for y in range(dim):
            if x == 0 or y == 0 or x == dim - 1 or y == dim - 1:
                cells[Point(x,y)] = CL_WALL()
            else:
                cells[Point(x,y)] = random_choose_weighted((9, CL_FLOOR), (1, CL_WALL))()

    return cells

def add_enemies(player, player_loc, cells, depth):
    ''' Generate enemies and place them on the level.
        Args:
            player (Player): The character controlled by the player.
            player_loc (Point): The location of the player.
            cells (map<Point, Cell>): A map of cells' locations to the contents of hte cells.
            depth (int): The depth of the level.
    '''
    assert player_loc != None
    assert player_loc in cells

    # spawn 1 mongoose per depth
    for i in range(depth):
        for i in range(10000): # eventually bail

            # repeatedly choose random cells
            loc, cell = choice(list(cells.items()))
            # discard ones that already have terrain or other actors
            if cell.is_full():
                continue
            # also discard those which can't get to the player, or which are too close
            to_player = a_star_search(cells, loc, player_loc, lambda cell: not cell.solid)
            if not to_player or len(to_player) < 4:
                continue

            # actually place an enemy
            cell.actor = Ghost()
            break
