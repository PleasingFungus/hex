''' Basic player character functionality. '''

from actor import Actor
import crender.colors

class Player(Actor):
    ''' The player character class.
    Attributes:
        alive (bool): Whether the player is alive or is dead (in the process of dying).
    '''

    def __init__(self):
        super().__init__('@', crender.colors.EMERALD)
        self.is_player = True
        self.alive = True
        self.is_mobile = True
        self.is_hittable = True # dubious

    def be_hit(self, other, history):
        ''' Be brutally battered.
        Args:
            other (Actor): The entity doing the damage.
            history (list<str>): The log.
        '''
        self.die(history)

    def die(self, history):
        ''' Be no longer alive.
        Args:
            history (list<str>): The log.
        '''

        history.append("You die...")
        self.alive = False
        # XXX: would be good to clear the input buffer here, or in things that call this
            # once we start properly buffering...

    def attempt_move(self, delta, area, history):
        ''' Attempt to move in the given direction.
        If there's an enemy there, hit it.
        If the move is successful, leave a trail behind.

        Params:
            delta (Point): The delta to move from the actor's current position.
            area (Area): The area the actor is in.
            history (list<str>): The log.
        Returns:
            Whether the player actually took time. (By moving and/or hitting.)
        '''

        # grab our previous loc first
        cur_loc = area.find_actor(self)
        assert cur_loc != None

        # check to see whether there's an enemy to murder
        did_hit = self.attempt_hit(delta, area, history)

        # actually try to move
        moved = super().attempt_move(delta, area, history)
        if not moved:
            return did_hit # still take time if you hit but didn't kill (this probably shouldn't happen?)

        # leave a trail
        assert cur_loc in area.cells
        old_cell = area.cells[cur_loc]
        assert old_cell.actor == None
        old_cell.actor = Actor('~', crender.colors.EMERALD)
        return True

    def attempt_hit(self, delta, area, history):
        ''' Attempt to bite whatever's in the given direction.
        Params:
            delta (Point): The delta to move from the actor's current position.
            area (Area): The area the actor is in.
            history (list<str>): The log.
        Returns:
            Whether the player actually hit anything.
        '''

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        target = delta + cur_loc
        if target not in area.cells:
            return False # can't hit outside the map!

        target_cell = area.cells[target]
        if not target_cell.actor or not target_cell.actor.is_hittable:
            return False # nothing to be hit

        history.append("You devour the mongoose!")
        target_cell.actor = None # XXX: this is killing the actor but will probably need to be generalized at some point
        return True
