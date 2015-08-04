''' A class abstracting a rendering & control-handling set of functions. '''

class VCState(object):
    ''' A glob of UI state.
    Attributes:
        io_handler (function<Player, Area, list<str> : tuple<bool, function<...>>>): A function that queries & handles one unit of player input.
    '''
    def __init__(self, io_handler):
        self.io_handler = io_handler

    def handle_io(self, area, player, history):
        ''' Prompt for input and handle the immediate results.
        Args:
            area (Area): The game map (cells).
            player (Player): The character controlled by the player.
            history (list<str>): The log.
        '''
        time_taken, io = self.io_handler(self, area, player, history)
        self.io_handler = io
        return time_taken

    def done(self):
        ''' Should the simulation terminate? '''
        return self.io_handler == None

    def render(self, area, player, history):
        ''' Render the current game state.
        Args:
            area (Area): The game map (cells).
            player (Player): The character controlled by the player.
            history (list<str>): The log.
        '''
        raise NotImplemented
