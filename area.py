''' Modelling game areas. '''

from cell import CL_FLOOR, CL_WALL
from point import Point
from rand import random2, choice

class Area(object):
    '''A set of terrain cells.
    
    Attributes:
        cells (dict<Point, Cell>): A map of Points to Cells comprising the Area.
    '''

    def __init__(self, cells):
        self.cells = cells

    def get_rows(self):
        ''' Build an ordering of the cells in the area.
        
        Returns:
            list<list<Cell>>: A list of rows of cells.
                              Each row is guaranteed to have uniform length.
                              Position in the lists indicates x & y positions.
                              Some row elements may be None, in the case of gaps.'''

        # XXX: consider caching this?

        rows = []
        for point, cell in self.cells.items():
            while len(rows) <= point.y:
                rows.append([])

            row = rows[point.y]
            while len(rows) <= point.x:
                row.append(None)

            row[point.x] = cell

        return rows

    @classmethod
    def gen_room(cls, dim):
        ''' Generate a completely random room of the given dimensions, starting from the origin.
        
        Args:
            dim (int): The number of rows & columns to generate.
        Returns:
            dict<Point, Cell>: A set of random cells completely filling the given dimensions.
        '''
        cells = {}
        for x in range(dim):
            for y in range(dim):
                cells[Point(x,y)] = choice([CL_FLOOR, CL_WALL])

        return cells
