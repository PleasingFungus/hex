''' Game interaction states. '''

from crender.crarea import render_area, render_sidebar, render_log

class VCState(object):
    ''' A single game state (e.g. moving, targeting jump, etc) for console,
    handling rendering, checking player IO, & mapping that into game state changes.
    Attributes:
        getkey (function<:str>): A function that fetches a single keypress from the player.
        windows (ConsoleWindows): A set of game windows.
        input_handler (function<str, Player, Area, list<str>: tuple<bool, class>>): The actual handler for player input.
    '''
    def __init__(self, getkey, windows, input_handler):
        self.getkey = getkey
        self.windows = windows
        self.input_handler = input_handler

    def render(self, player, area, history):
        ''' Render the game state to the console.
        Args:
            player (Player): The character controlled by the player.
            area (Area): The game map (cells).
            history (list<str>): The log.            
        '''
        self.main_render(area)
        self.sidebar_render(player, area)
        self.log_render(history)    
    
    def main_render(self, area):
        ''' Render the game map, characters, etc.
        Args:
            area (Area): The game map (cells)
        '''
        render_area(area, self.windows.main)

    def sidebar_render(self, player, area):
        ''' Render the sidebar (other info).
        Args:
            player (Player): The character controlled by the player.
            area (Area): The game map (cells).
        '''
        render_sidebar(player, area, self.windows.sidebar)

    def log_render(self, history):
        ''' Render the game log.
        Args:
            history (list<str>): The text of the log.
        '''
        render_log(history, self.windows.log)

    def handle_io(self, player, area, history):
        ''' Request player input and map it to game changes.
        Args:
            player (Player): The character controlled by the player.
            area (Area): The game map (cells).
            history (list<str>): The log.
        Returns:
            tuple<bool, VCState>: Whether the player took time, and a handler for the next input/render cycle.
            The handler may be None, in which case the game should terminate.
        '''
        took_time, next_state = self.input_handler(self.getkey(), player, area, history)
        return took_time, self.clone(next_state)

    def clone(self, next_class):
        ''' Create an instance of the next state with this one's attributes. '''
        if not next_class:
            return None
        return next_class(self.getkey, self.windows)
