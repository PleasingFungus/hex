''' Main snake game running processes. '''

from area import Area
from dungeon import new_level
from player import Player
from point import Point
from vcstate import VCWrapper

level_dim = 19

def run_game(vcstate):
    ''' The main game loop.
        Params:
            vcstate: An object that handles rendering & IO.
    '''
    halfwidth = int(level_dim / 2)
    midpoint = Point(halfwidth, halfwidth)
    player = Player()
    area = Area(new_level(player, midpoint, 1, level_dim))
    history = ['']

    vcwrapper = VCWrapper(vcstate)

    while True:
        # render & check IO
        vcwrapper.vcstate.render(player, area, history)
        time_taken = vcwrapper.run(player, area, history)

        if vcwrapper.done():
            return
        if not time_taken:
            continue

        # cooldowns
        for abil in player.abilities:
            abil.cooldown = max(0, abil.cooldown - 1)

        # run the rest of the simulation
        if on_stairs(player, area):
            move_to_new_level(player, area, history)
            continue

        for actor in area.all_actors():
            actor.act(area, history)
            # XXX: don't let actors randomly block each-other based on invisible ordering

def on_stairs(player, area):
    ''' Is the player is on the stairs to the next level?
        Args:
            player (Player): The character controlled by the player.
            area (Area): The current level.
        Returns:
            bool: Whether the player is on the stairs.
    '''

    loc = area.find_actor(player)
    assert loc != None
    assert loc in area.cells

    cell = area.cells[loc]
    return cell.is_stairs

def move_to_new_level(player, area, history):
    ''' Handle the player moving to a new level.
        Args:
            player (Player): The character controlled by the player.
            area (Area): The current level.
            history (list<str>): The log.
    '''
    loc = area.find_actor(player)
    assert loc != None
    assert loc in area.cells

    area.depth += 1
    area.cells = new_level(player, loc, area.depth, level_dim)
    history.append("Welcome to level {}!".format(area.depth))

    # give the player a little health back
    healed = player.heal(1)
    if healed:
        history[-1] += " You feel a little better."

