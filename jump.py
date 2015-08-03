''' Let the player jump, or try. '''

JUMP_RANGE = 2

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
    target_tile = area.cells.get(target_loc)
    if not target_tile:
        return False # can't jump outside the map!

    if target_tile.is_full():
        history.append("There's already something there!")
        return False

    success = player.attempt_move(delta, area, history)
    assert success
    return True
