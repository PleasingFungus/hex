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
