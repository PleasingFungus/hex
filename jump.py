''' Let the player jump, or try. '''

from ability import ABIL_JUMP

JUMP_RANGE = 2
JUMP_COOLDOWN = 3

def attempt_jump(direction, player, area, history):
    ''' Attempt to 'jump' the player in the given direction.
    Fails if the tile is occupied.

    Args:
        direction (Point): The direction in which to jump.
        player (Actor): The character the player controls.
        area (Area): The area the character inhabits.
        history (list<str>): The log.
    '''

    delta = direction.scaled(JUMP_RANGE)
    assert delta.abs() == JUMP_RANGE

    player_loc = area.find_actor(player)
    assert player_loc

    target_loc = player_loc + delta
    target_cell = area.cells.get(target_loc)
    if not target_cell:
        return False # can't jump outside the map!

    if target_cell.is_full():
        history.append("There's already something there!")
        return False

    assert valid_jump_destination(target_cell)

    success = player.attempt_move(delta, area, history)
    assert success
    player.get_abil(ABIL_JUMP).cooldown = JUMP_COOLDOWN
    return True

def valid_jump_destination(cell):
    ''' Diregarding distance from the player, is the given
    cell a valid target?
    Args:
        cell (Cell): The cell in question.
    Returns:
        bool: Whether the cell can be jumped into.
    '''

    if not cell:
        return False # can't jump outside the map!

    if cell.is_full():
        return False # can't jump into an occupied cell!

    return True

