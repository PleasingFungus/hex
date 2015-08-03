''' The console-based launcher for the game. '''

import curses
import logging

from cinput.cimove import handle_move_input
from crender.crarea import render_area, render_sidebar, render_log
from snake import run_game
from quit import QuitException

def main(scr):
    ''' Run the game. '''
    curses.curs_set(0)

    sidebar_width = 12
    main_width = curses.COLS - sidebar_width
    log_height = 5
    main_height = curses.LINES - log_height
    sidebar_window = curses.newwin(main_height, sidebar_width, 0, 0)
    main_window = curses.newwin(main_height, main_width, 0, sidebar_width)
    log_window = curses.newwin(log_height, curses.COLS, main_height, 0)

    main_render = lambda area: render_area(area, main_window)
    sidebar_render = lambda player,area: render_sidebar(player, area, sidebar_window)
    log_render = lambda history: render_log(history, log_window)
    # FIXME: this displays black until the player provides input (???)
        # only true if querying 'scr'; however, querying others doesn't get arrow presses
    io = make_io(scr, handle_move_input)

    curses.ungetch('~') # hack to 'fix' the above ^

    run_game(main_render, sidebar_render, log_render, io)

def make_io(scr, iofunc):
    ''' Take a function and wrap it for use by the main game loop.
    Args:
        scr: A curses screen to be queried for input.
        iofunc (function<str, Player, Area, list<str> : bool>): A function that takes input and transforms it into game state changes.
    Returns:
        function<Player, Area, list<str> : bool>: The wrapped function without the 'command' argument.
    '''

    return (lambda player, area, history: iofunc(scr.getkey(), player, area, history))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    try:
        curses.wrapper(main)
    except QuitException:
        print("Have a nice day!")
