''' Modelling individual terrain cells. '''

class Cell(object):
    '''A terrain cell.
    
    Attributes:
        glyph (str): the text glyph for the cell.
        full (bool): whether the cell is occupied, or can be entered.
    '''
    def __init__(self, glyph, full):
        self.glyph = glyph
        self.full = full

CL_FLOOR = Cell('.', False)
CL_WALL = Cell('▓', True)
