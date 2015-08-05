''' A* pathfinding. '''

from queue import PriorityQueue

def a_star_search(cells, start, goal, passable_metric):
    ''' Find the fastest path from the start to the goal in the given area.
    A slightly modified version of http://www.redblobgames.com/pathfinding/a-star/implementation.html .

    Args:
        cells (dict<Point, Cell>): A map of points (locations) to cells.
        start (Point): The starting point of the search.
        goal (Point): The intended destination of the search.
        passable_metric (function<Cell:bool>): A function returning True iff a cell can be pathed through.
    Returns:
        An ordered list of points to travel to reach the goal.
        Includes the goal, but does not include the start.
    '''
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break

        if not passable_metric(cells[current]):
            continue # don't path through impassable cells!
        
        neighbors = [loc for loc in cells if loc.adjacent(current)] # inefficient
        for next_loc in neighbors:
            new_cost = cost_so_far[current] + 1
            if next_loc not in cost_so_far or new_cost < cost_so_far[next_loc]:
                cost_so_far[next_loc] = new_cost
                priority = new_cost + (goal - next_loc).abs()
                frontier.put(next_loc, priority)
                came_from[next_loc] = current

    if goal not in came_from: # couldn't find any path
        return None

    path = [goal]
    while came_from[path[-1]] != start:
        path.append(came_from[path[-1]])
    return list(reversed(path))
