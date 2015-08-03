''' The console-based launcher for the game. '''

import curses
import logging

from cinput.cimove import MoveInputHandler
from crender.cwindows import ConsoleWindows
from snake import run_game

def main(scr):
    ''' Run the game. '''
    curses.curs_set(0)

    windows = ConsoleWindows()
    io = MoveInputHandler(scr.getkey, windows)

    # FIXME: using multiple windows displays black until the player provides input (???)
        # only true if querying 'scr' for getkey(); however, querying others doesn't get arrow presses
    curses.ungetch('~') # hack to 'fix' the above ^ (assumes ~ won't be bound to any function)

    run_game(io)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    curses.wrapper(main)
    print("Have a nice day!")
