''' Actor class & methods. '''

from point import add_points

class Actor(object):
    ''' An entity that occupies a Cell.
    '''
    def __init__(self):
        pass

    def cur_glyph(self):
        ''' What glyph should currently be used to represent this actor in the console?
        Returns:
            The correct glyph for the actor; e.g. '@'.
        '''
        return '@'

    def attempt_move(self, delta, area):
        ''' Attempt to move the actor the given delta from their current position in the current area.

        Args:
            delta (Point): The delta to move from the actor's current position.
            area (Area): The area the actor is in.
        Returns:
            bool: Whether the actor successfully moved.
        '''

        cur_loc = area.find_actor(self)
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
        new_cell.actor = self
        return True
