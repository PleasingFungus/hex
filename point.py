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
        ''' Negate a point as a vector (flip across the origin '''
        return Point(-self.x, -self.y)

    def __sub__(a, b):
        ''' Subtract two points as vectors. '''
        return Point(a.x - b.x, a.y - b.y)

    def __repr__(self):
        return "<Point({},{})>".format(self.x, self.y)
