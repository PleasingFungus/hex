''' Basic player input command functionality. '''

from getch import getch
from point import Point

def move_comm(x, y):
    ''' Generate a movement command for the corresponding delta.
    Args:
        x (int): The x-movement in question. (E.g., 1 to move right)
        y (int): The y-movement in question. (E.g., -1 to move up)
    Returns:
        function<Player, Area>: A function that tries to move the player in the corresponding direction.
    '''
    delta = Point(x, y)
    def move(player, area):
        return (player.attempt_move(delta, area), False)
    return move

commands = {'y' : move_comm(0, -1), 'n' : move_comm(0, 1),
            'h' : move_comm(-1, 0), 'j' : move_comm(1, 0),
            'KEY_UP' : move_comm(0, -1), 'KEY_DOWN' : move_comm(0, 1),
            'KEY_LEFT' : move_comm(-1, 0), 'KEY_RIGHT' : move_comm(1, 0),
            'q' : (lambda _,__: (False, True)), 'd' : (lambda player,_: (player.die(), False)) }

def go(command, player, area):
    ''' Respond appropriately to player input.
    
    Args:
        command (str): The command in question.
        player (Actor): The character the player controls.
        area (Area): The area the character inhabits.
    Returns:
        tuple<bool, bool>: Whether the command took time, and whether the game should exit.
    '''
    if not player.alive:
        return (False, True) # quit without responding to input

    if command in commands:
        took_time, should_quit = commands[command](player, area)
        return (took_time, should_quit)
    return (False, False)
