''' Basic player input command functionality. '''

from getch import getch
from point import Point
from quit import QuitException

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

def quit(_, __,___):
    raise QuitException

commands = {'y' : move_comm(0, -1), 'n' : move_comm(0, 1),
            'h' : move_comm(-1, 0), 'j' : move_comm(1, 0),
            'KEY_UP' : move_comm(0, -1), 'KEY_DOWN' : move_comm(0, 1),
            'KEY_LEFT' : move_comm(-1, 0), 'KEY_RIGHT' : move_comm(1, 0),
            'q' : quit, 'd' : (lambda player,_,history: player.die(history)) }

def go(command, player, area, history):
    ''' Respond appropriately to player input.
    
    Args:
        command (str): The command in question.
        player (Actor): The character the player controls.
        area (Area): The area the character inhabits.
        history (list<str>): The log.
    Returns:
        bool: Whether the command took time.
    '''
    if not player.is_alive():
        raise QuitException # quit without responding to input

    if command in commands:
        took_time = commands[command](player, area, history)
        return took_time
    return False # unbound commands take no time
