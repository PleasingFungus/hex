''' Modelling basic geometry. '''

class Point(object):
    '''A 2D point.

    Attributes:
        x (int): The column of the point.
        y (int): The row of the point.
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(a, b):
        ''' Sum two points as vectors. '''
        return Point(a.x + b.x, a.y + b.y)

    def __neg__(self):
        ''' Negate a point as a vector (flip across the origin) '''
        return Point(-self.x, -self.y)

    def __sub__(a, b):
        ''' Subtract two points as vectors. '''
        return Point(a.x - b.x, a.y - b.y)

    def __repr__(self):
        return "<Point({},{})>".format(self.x, self.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def adjacent(self, other):
        ''' Is this point adjacent to the other point in the current metric?
        Would need to be changed in a hex or 8-direction metric.

        Args:
            other (Point): The point to be checked for adjacency.
        Returns:
            bool: Whether the other point is directly adjacent to this one.
                  A point is not considered adjacent to itself.
        '''

        return (other.x == self.x and abs(other.y - self.y) == 1
             or other.y == self.y and abs(other.x - self.x) == 1)

    def abs(self):
        ''' The absolute distance from the origin. '''
        return abs(self.x) + abs(self.y)

    def scaled(self, length):
        ''' Return a version of this point (as a vector) with the provided length.
        Expect integer rounding errors. '''
        cur_len = self.abs()
        return Point(int(self.x * length / cur_len), int(self.y * length / cur_len))
