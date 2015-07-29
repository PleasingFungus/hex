''' Modelling individual terrain cells. '''

# TODO: move loc into actors instead, to preserve 1 loc per actor invariant

class Cell(object):
    '''A terrain cell.
    
    Attributes:
        glyph (str): the text glyph for the cell.
        solid (bool): whether the cell is totally solid (e.g. a wall), or can be entered.
        actor (Actor): the actor currently occupying the cell; may be None.
        is_stairs (bool): whether the player can walk down this tile to the next level.
    '''
    def __init__(self, glyph, solid):
        self.glyph = glyph
        self.solid = solid
        self.actor = None
        self.is_stairs = False

    def cur_glyph(self):
        ''' Get the current console glyph for the cell.
        Returns:
            (str): The glyph for the current actor in the cell, if any, or the glyph for the cell otherwise.
        '''
        return self.actor.cur_glyph() if self.actor else self.glyph

    def is_full(self):
        ''' Is the cell currently full (un-enterable)?
        Returns:
            Whether the cell is impossible for any (further) actors to enter.
        '''
        return self.solid or self.actor

class Stairs(Cell):
    ''' A set of stairs leading to the next level. '''
    def __init__(self):
        super().__init__('>', False)
        self.is_stairs = True

CL_FLOOR = lambda: Cell('.', False)
CL_WALL = lambda: Cell('#', True)
CL_STAIR = Stairs
