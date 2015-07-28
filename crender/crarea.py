''' Functions for rendering an area to the console.'''

def stringify_row(row):
    ''' Turn a given row of Cells into a printable string.

    Args:
        row (list<Cell>): An ordered list of cells, representing a continuous series of Cells with the same y-value.
                          Some may be None.
    Returns:
        str: A representation of the row; e.g. '...###.#  #...#'
    '''
    return ''.join((cell.glyph if cell else ' ') for cell in row)

def render_area(area):
    ''' Render a given Area to the console.
    
    Args:
        area (Area): The Area in question.
    '''
    # sort the area into rows
    rows = area.get_rows()
    # build a set of strings from the rows
    str_rows = [stringify_row(row) for row in rows]
    # render the rows to the console
    print('\n'.join(str_rows))
