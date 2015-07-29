''' Actor class & methods. '''

import crender.colors

class Actor(object):
    ''' An entity that occupies a Cell.
        Attributes:
            glyph (str): The glyph used to represent the actor in console; e.g. '@'.
            color (Color): The color pair used for the console glyph; defaults to white.
    '''
    def __init__(self, glyph, color=crender.colors.WHITE):
        self.glyph = glyph
        self.color = color

    def cur_glyph(self):
        ''' What glyph should currently be used to represent this actor in the console?
        Returns:
            str: The correct glyph for the actor; e.g. '@'.
        '''
        return self.glyph

    def cur_color(self):
        ''' What color should currently be used for this actor's glyph in the console?
        Returns:
            int: The correct color pair for the actor; e.g. 0 (white).
        '''
        return self.color

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

        new_loc = cur_loc + delta
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
