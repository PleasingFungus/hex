''' Functions for rendering an area to the console.'''

from curses import color_pair

def render_area(area, scr):
    ''' Render a given Area to the console.
    
    Args:
        area (Area): The Area in question.
        scr: the curses screen to be rendered to.
    '''
    scr.clear()
    for loc, cell in area.cells.items():
        scr.addch(loc.x, loc.y, ord(cell.cur_glyph()), color_pair(cell.cur_color()))
        # TODO: support extended ascii/unicode ^ 
    scr.refresh()
