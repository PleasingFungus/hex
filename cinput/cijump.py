''' Let the player select a jump target or cancel. '''

from functools import partial

from jump import attempt_jump
from point import Point

# TODO: implement check cooldowns
def prompt_jump(_, __, history):
    ''' Print a jump prompt to the log.
    Args:
        history (list<str>): The log.
    Returns:
        bool: False. (Whether this took time.)
    '''
    history.append("Press a direction to jump, or any other key to abort.")
    return False # doesn't take time

# TODO: abstract & share this with cimove's version
directions = {'y' : Point(0, -1), 'n' : Point(0, 1),
              'h' : Point(-1, 0), 'j' : Point(1, 0),
              'KEY_UP' : Point(0, -1), 'KEY_DOWN' : Point(0, 1),
              'KEY_LEFT' : Point(-1, 0), 'KEY_RIGHT' : Point(1, 0)}

def handle_jump_input(getkey, player, area, history):
    ''' Prompt for input and either select a jump location (and jump there) or abort.
    
    Args:
        getkey (function<str>): A function to fetch a single character of player input.
        player (Actor): The character the player controls.
        area (Area): The area the character inhabits.
        history (list<str>): The log.
    Returns:
        tuple<bool, function<Player, Area, list<str> : tuple<...>>>: Whether the command took time, and a function to call for next input.
        The function may be None, in which case the game should terminate.
    '''
    command = getkey()

    from cinput.cimove import handle_move_input # do this here to avoid a loop

    if command not in directions: # if some random key was pressed
        history.append("Okay, then.")
        return False, partial(handle_move_input, getkey) # abort selection (don't take time)

    jumped = attempt_jump(directions[command], player, area, history)
    if not jumped:
        return False, partial(handle_jump_input, getkey) # try again if the player prompted an invalid direction
    return True, partial(handle_move_input, getkey)
