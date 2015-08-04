''' The console-based launcher for the game. '''

import curses
import logging

from cinput.cimove import handle_move_input
from crender.crarea import render_area, render_sidebar, render_log
from crender.cwindows import ConsoleWindows
from snake import run_game

def main(scr):
    ''' Run the game. '''
    curses.curs_set(0)

    windows = ConsoleWindows()

    main_render = lambda area: render_area(area, windows.main)
    sidebar_render = lambda player,area: render_sidebar(player, area, windows.sidebar)
    log_render = lambda history: render_log(history, windows.log)
    # FIXME: this displays black until the player provides input (???)
        # only true if querying 'scr'; however, querying others doesn't get arrow presses
    io = lambda player, area, history: handle_move_input(scr.getkey, player, area, history)

    curses.ungetch('~') # hack to 'fix' the above ^

    run_game(main_render, sidebar_render, log_render, io)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    curses.wrapper(main)
    print("Have a nice day!")
