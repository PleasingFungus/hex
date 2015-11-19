''' A class abstracting a rendering & control-handling set of functions. '''

class VCWrapper(object):
    ''' A wrapper around rendering & control-handling functions.
    Attributes:
        vcstate: An object with render() & handle_io() functions.'''
    def __init__(self, vcstate):
        self.vcstate = vcstate

    def run(self, player, area, history):
        ''' Prompt for input, and handle the immediate results.
        Args:
            player (Player): The character controlled by the player.
            area (Area): The game map (cells).
            history (list<str>): The log.
        '''

        time_taken, vcstate = self.vcstate.handle_io(player, area, history)
        self.vcstate = vcstate
        return time_taken

    def done(self):
        ''' Should the simulation terminate? '''
        return self.vcstate == None
