''' Setup color for a screen. '''

import curses

mapped_pairs = {}

class Color(object):
    ''' An abstraction layer for a curses color modifier code.
        Attributes:
            bright (bool): Whether the color should be displayed bright (bolded).
            fg (int): The foreground color; e.g. curses.COLOR_WHITE.
            bg (int): The background color; e.g. curses.COLOR_BLACK.
    '''

    def __init__(self, bright, fg, bg = curses.COLOR_BLACK):
        self.bright = bright
        self.fg = fg
        self.bg = bg

    def pair_id(self):
        ''' Find the pair ID for this color (fg,bg tuple). If it doesn't exist, create it.
        Returns:
            int: An ID that can be used for curses.color_pair.
        '''
        pair = (self.fg, self.bg)
        if pair not in mapped_pairs:
            pair_id = len(mapped_pairs)
            curses.init_pair(pair_id, self.fg, self.bg) # this might crash if we run out of pairs to map - oops
            mapped_pairs[pair] = pair_id
        return mapped_pairs[pair]

    def attribute_code(self):
        ''' The modifier code used to display glyphs in this color.
        Returns:
            int: an attribute code. (See curses documentation.)
        '''

        code = curses.color_pair(self.pair_id())
        if self.bright:
            return code ^ curses.A_BOLD
        return code

WHITE = Color(False, curses.COLOR_WHITE)
BWHITE = Color(True, curses.COLOR_WHITE)
BROWN = Color(False, curses.COLOR_YELLOW)
YELLOW = Color(True, curses.COLOR_YELLOW)
FOREST = Color(False, curses.COLOR_GREEN)
EMERALD = Color(True, curses.COLOR_GREEN)
RUST = Color(False, curses.COLOR_RED)
RED = Color(True, curses.COLOR_RED)
PURPLE = Color(False, curses.COLOR_MAGENTA)
MAGENTA = Color(True, curses.COLOR_MAGENTA)

mapped_pairs[(WHITE.fg, WHITE.bg)] = 0 # predefined
