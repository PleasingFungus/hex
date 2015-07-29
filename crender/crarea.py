''' Functions for rendering an area to the console.'''

def render_area(area, scr):
    ''' Render a given Area to the console.
    
    Args:
        area (Area): The Area in question.
        scr: the curses screen to be rendered to.
    '''
    scr.clear()
    for loc, cell in area.cells.items():
        scr.addstr(loc.y, loc.x, cell.cur_glyph().encode('utf-8'), cell.cur_color().attribute_code())
    scr.refresh()

def render_sidebar(player, area, scr):
    ''' Render a given Player & Area's metadata to the console.

    Args:
        player (Player): The Player in question.
        area (Area): The Area in question.
        scr: the curses screen to be rendered to.
    '''
    scr.clear()

    if not player.alive:
        scr.addstr(0, 0, "You died!")
        scr.refresh()
        return

    scr.addstr(0, 0, "Depth: {}".format(area.depth))
    scr.refresh()
