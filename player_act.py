''' Player actions. '''

from point import add_points

# XXX: merge this into actor proper

def attempt_move(actor, delta, area):
    ''' Attempt to move the actor the given delta from their current position in the current area.

    Args:
        actor (Actor): The actor to be moved.
        delta (Point): The delta to move from the actor's current position.
        area (Area): The area the actor is in.
    Returns:
        bool: Whether the actor successfully moved.
    '''

    cur_loc = area.find_actor(actor)
    assert cur_loc != None

    new_loc = add_points(cur_loc, delta)
    if new_loc not in area.cells: # OOB
        return False
    
    new_cell = area.cells[new_loc]
    if new_cell.is_full(): # solid or occupied
        return False
    
    # let's move!
    cur_cell = area.cells[cur_loc]
    assert cur_cell
    cur_cell.actor = None
    new_cell.actor = actor
    return True
