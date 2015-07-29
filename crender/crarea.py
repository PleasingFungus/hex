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
