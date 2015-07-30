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

def debug_astar(area, scr):
    player = [actor for actor in area.all_actors() if actor.is_player][0]
    mongoose = [actor for actor in area.all_actors() if actor.glyph == 'o'][0]
    mongoose_loc = area.find_actor(mongoose)
    player_loc = area.find_actor(player)
    from astar import a_star_search
    path = a_star_search(area.cells, mongoose_loc, player_loc) or []
    for p in path:
        scr.addstr(p.y, p.x, '*'.encode('utf-8'))

def render_sidebar(player, area, scr):
    ''' Render a given Player & Area's metadata to the console.

    Args:
        player (Player): The Player in question.
        area (Area): The Area in question.
        scr: the curses screen to be rendered to.
    '''
    scr.clear()

    scr.addstr(0, 0, "Depth: {}".format(area.depth))
    if not player.alive:
        scr.addstr(1, 0, " R I P ")

    scr.refresh()

def render_log(history, scr):
    ''' Render the log to the console.
    Args:
        history (list<str>): The log.
        scr: The curses screen to be rendered to.
    '''
    scr.clear()

    height, _ = scr.getmaxyx()
    for i, line in enumerate(history[-height:]):
        scr.addstr(i, 0, line)

    scr.refresh()

