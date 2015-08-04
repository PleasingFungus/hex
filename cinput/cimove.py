''' Basic player input command functionality. '''

from cinput.cijump import prompt_jump, JumpInputHandler
from cinput.ciabil import ConsoleAbility
from cinput.vcstate import VCState
from getch import getch
from point import Point

def move_comm(x, y):
    ''' Generate a movement command for the corresponding delta.
    Args:
        x (int): The x-movement in question. (E.g., 1 to move right)
        y (int): The y-movement in question. (E.g., -1 to move up)
    Returns:
        function<Player, Area, list<str>>: A function that tries to move the player in the corresponding direction.
    '''
    delta = Point(x, y)
    def move(player, area, history):
        return player.attempt_move(delta, area, history)
    return move

basic_commands = {'y' : move_comm(0, -1), 'n' : move_comm(0, 1),
                  'h' : move_comm(-1, 0), 'j' : move_comm(1, 0),
                  'KEY_UP' : move_comm(0, -1), 'KEY_DOWN' : move_comm(0, 1),
                  'KEY_LEFT' : move_comm(-1, 0), 'KEY_RIGHT' : move_comm(1, 0),
                  'd' : (lambda player,_,history: player.die(history)) }

basic_state_changes = { 'q' : None }

def nil_command(*_):
    return False

for key in basic_state_changes:
    if key not in basic_commands:
        basic_commands[key] = nil_command

def handle_move_input(command, player, area, history):
    ''' Respond appropriately to player input.
    
    Args:
        command (str): A single keypress of player input.
        player (Actor): The character the player controls.
        area (Area): The area the character inhabits.
        history (list<str>): The log.
    Returns:
        tuple<bool, class>: Whether the command took time, and a handler for the next input/render cycle.
        The class may be None, in which case the game should terminate.
    '''
    if not player.is_alive():
        return False, None # quit without responding to player input

    abilities = [ConsoleAbility(abil.idstr) for abil in player.abilities]

    commands = basic_commands.copy()
    commands.update({a.hotkey() : a.on_activate() for a in abilities})
    # TODO: respect cooldowns

    next_state = MoveInputHandler
    state_changes = basic_state_changes.copy()
    state_changes.update({a.hotkey() : (a.state_change() or next_state) for a in abilities})

    if command in commands:
        took_time = commands[command](player, area, history)
        next_state = state_changes.get(command, next_state)
        return took_time, next_state
    return False, next_state # unbound commands take no time

class MoveInputHandler(VCState):
    def __init__(self, getkey, windows):
        super().__init__(getkey, windows, handle_move_input)
