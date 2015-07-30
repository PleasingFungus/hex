''' Modelling game areas. '''

from cell import CL_FLOOR, CL_WALL, CL_STAIR
from point import Point
from rand import random2, choice

class Area(object):
    '''A set of terrain cells.
    
    Attributes:
        cells (dict<Point, Cell>): A map of Points to Cells comprising the Area.
        depth (int): The level number, starting from 1 and incrementing each time the player descends.
    '''

    def __init__(self, cells, depth=1):
        self.cells = cells
        self.depth = depth

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

            while len(row) <= point.x:
                row.append(None)
            row[point.x] = cell

        return rows

    def find_actor(self, actor):
        ''' Return the coordinates of the given actor in this area.
        Args:
            actor (Actor): The actor in question.
        Returns:
            Point: The location of the actor, or None if they're not found.
        '''
        for loc, cell in self.cells.items():
            if cell.actor == actor:
                return loc
        return None

    def all_actors(self):
        ''' Find all actors currently within the area.
        Returns:
            list<Actor>: A list of actors in the cells of the area. Order semirandom and not guaranteed consistent between calls.
        '''
        return [cell.actor for cell in self.cells.values() if cell.actor]

    def get_player(self):
        ''' Find the player.
        Asserts that there is one and exactly one player present.
        Returns:
            Player: An actor in the area that has is_player set.
        '''
        players = [a for a in self.all_actors() if a.is_player]
        assert len(players) == 1
        return players[0]

    @classmethod
    def gen_room(cls, dim):
        ''' Generate a completely hollow room of the given dimensions, starting from the origin.
        
        Args:
            dim (int): The number of rows & columns to generate.
        Returns:
            dict<Point, Cell>: A set of cells completely filling the given dimensions.
        '''
        cells = {}
        for x in range(dim):
            for y in range(dim):
                if x == 0 or y == 0 or x == dim - 1 or y == dim - 1:
                    cells[Point(x,y)] = CL_WALL()
                else:
                    cells[Point(x,y)] = CL_FLOOR()

        cells[Point(int(dim/2), 1)] = CL_STAIR()

        return cells
