''' Actor class & methods. '''

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
