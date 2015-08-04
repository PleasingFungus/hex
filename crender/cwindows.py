''' Setup & store curses windows. '''

import curses

class ConsoleWindows(object):
    ''' A holder for curses screens.
    Attributes:
        main: The main display (for the map, &c).
        sidebar: The sidebar, for abilties, location, etc.
        log: the bottom bar, for the log.
    '''
    def __init__(self):
        sidebar_width = 12
        main_width = curses.COLS - sidebar_width
        log_height = 5
        main_height = curses.LINES - log_height

        self.sidebar = curses.newwin(main_height, sidebar_width, 0, 0)
        self.main = curses.newwin(main_height, main_width, 0, sidebar_width)
        self.log = curses.newwin(log_height, curses.COLS, main_height, 0)
