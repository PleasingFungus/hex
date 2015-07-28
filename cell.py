''' Modelling individual terrain cells. '''

class Cell(object):
    '''A terrain cell.
    
    Attributes:
        glyph (str): the text glyph for the cell.
        solid (bool): whether the cell is totally solid (e.g. a wall), or can be entered.
        actor (Actor): the actor currently occupying the cell; may be None.
    '''
    def __init__(self, glyph, solid):
        self.glyph = glyph
        self.solid = solid
        self.actor = None

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

CL_FLOOR = lambda: Cell('.', False)
CL_WALL = lambda: Cell('▓', True)
