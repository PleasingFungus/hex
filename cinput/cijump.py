''' Let the player select a jump target or cancel. '''

from cinput.vcstate import VCState
from crender.crjump import render_jump_targets
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

def handle_jump_input(command, player, area, history):
    ''' Prompt for input and either select a jump location (and jump there) or abort.
    
    Args:
        command (str): A single keypress of player input.
        player (Actor): The character the player controls.
        area (Area): The area the character inhabits.
        history (list<str>): The log.
    Returns:
        tuple<bool, class>: Whether the action took time, and the next input/rendering state to enter.
        The state may be None, in which case the game should terminate.
    '''
    from cinput.cimove import MoveInputHandler # do this here to avoid a loop

    if command not in directions: # if some random key was pressed
        history.append("Okay, then.")
        return False, MoveInputHandler # abort selection (don't take time)

    jumped = attempt_jump(directions[command], player, area, history)
    if not jumped:
        return False, MoveInputHandler
    return True, MoveInputHandler

class JumpInputHandler(VCState):
    def __init__(self, getkey, windows):
        super().__init__(getkey, windows, handle_jump_input)

    def main_render(self, area):
        ''' Render the game map, characters, etc.
        Args:
            area (Area): The game map (cells)
        '''
        super().main_render(area)
        render_jump_targets(area, self.windows.main)
