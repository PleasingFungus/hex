''' Basic player input command functionality. '''

from getch import getch
from point import Point

def move_comm(delta):
    ''' Generate a movement command for the corresponding delta.
    Args:
        delta (Point): The movement in question. (E.g. Point(0, 1) to move down)
    Returns:
        function: A function that tries to move the player in the corresponding direction.
    '''
    def move(player, area):
        player.attempt_move(delta, area)
        return False
    return move

commands = {'y' : move_comm(Point(0, -1)), 'n' : move_comm(Point(0, 1)),
            'g' : move_comm(Point(-1, 0)), 'j' : move_comm(Point(1, 0)),
            'q' : (lambda a,b: True) }

def go(player, area):
    ''' Prompt for player input and respond accordingly.
    
    Args:
        player (Actor): The character the player controls.
        area (Area): The area the character inhabits.
    '''
    command = getch()
    if command in commands:
        should_quit = commands[command](player, area)
        return should_quit
    return False
