''' Special rendering for jump targeting. '''

from crender import colors
from jump import JUMP_RANGE, valid_jump_destination

def render_jump_targets(area, scr):
    ''' Indicate all valid jump targets on the map.
    Args:
        area (Area): The map.
        scr: A curses screen to render to.
    '''

    player_loc = area.find_actor(area.get_player())
    
    for target, cell in area.cells.items():
        delta = target - player_loc
        if ((abs(delta.x) != JUMP_RANGE or delta.y) and
            (abs(delta.y) != JUMP_RANGE or delta.x)):
            continue

        if not valid_jump_destination(cell):
            continue

        scr.addstr(target.y, target.x, '*'.encode('utf-8'), colors.YELLOW.attribute_code())

    scr.refresh()
