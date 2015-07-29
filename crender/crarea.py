''' Functions for rendering an area to the console.'''

def render_area(area, scr):
    ''' Render a given Area to the console.
    
    Args:
        area (Area): The Area in question.
        scr: the curses screen to be rendered to.
    '''
    scr.clear()
    for loc, cell in area.cells.items():
        scr.addch(loc.y, loc.x, ord(cell.cur_glyph()), cell.cur_color().attribute_code())
        # TODO: support extended ascii/unicode ^ 
    scr.refresh()
