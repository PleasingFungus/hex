''' Basic player character functionality. '''

from actor import Actor
import crender.colors

class Player(Actor):
    ''' The player character class. '''

    def __init__(self):
        super().__init__('@', crender.colors.EMERALD)

    def attempt_move(self, delta, area):
        ''' Attempt to move in the given direction.
            If successful, leave a trail behind.
            Params: 
        '''

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        moved = super().attempt_move(delta, area)
        if not moved:
            return

        # leave a trail
        assert cur_loc in area.cells
        old_cell = area.cells[cur_loc]
        assert old_cell.actor == None
        old_cell.actor = Actor('~', crender.colors.EMERALD)
