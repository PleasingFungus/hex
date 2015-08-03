''' Main snake game running processes. '''

from area import Area
from dungeon import new_level
from player import Player
from point import Point

level_dim = 19

def run_game(main_render, sidebar_render, log_render, io):
    ''' The main game loop.
        Params:
            main_render (function<Area>): Render the current game state to the screen.
            sidebar_render (function<Player, Area>): Render metadata to the sidebar.
            log_render (function<list<str>>): Render history data to the player.
            io (function<Player, Area>): Query the player for their next action.
    '''
    halfwidth = int(level_dim / 2)
    midpoint = Point(halfwidth, halfwidth)
    player = Player()
    area = Area(new_level(player, midpoint, 1, level_dim))
    history = ['']

    while True:
        main_render(area)
        sidebar_render(player, area)
        log_render(history)

        # TODO: support varying rendering by io state (for e.g. abil prompts)
        time_taken, io = io(player, area, history)
        if not io:
            return
        if not time_taken:
            continue

        check_stairs(player, area, history)
        for actor in area.all_actors():
            actor.act(area, history)

def check_stairs(player, area, history):
    ''' Check if the player is on the stairs.
        If so, generate a new level.
        Args:
            player (Player): The character controlled by the player.
            area (Area): The current level.
            history (list<str>): The log.
    '''

    loc = area.find_actor(player)
    assert loc != None
    assert loc in area.cells

    cell = area.cells[loc]
    if not cell.is_stairs:
        return

    # on the stairs; new level.
    area.depth += 1
    area.cells = new_level(player, loc, area.depth, level_dim)
    history.append("Welcome to level {}!".format(area.depth))

    # give the player a little health back
    player.heal(1)

