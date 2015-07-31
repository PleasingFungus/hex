''' Basic player character functionality. '''

from actor import Actor
import crender.colors

MAX_HP = 3

class Player(Actor):
    ''' The player character class.
    Attributes:
        health (int): The player's current HP; 0 implies dead.
    '''

    def __init__(self):
        super().__init__("player", None)
        self.health = MAX_HP

    def is_player(self):
        """ This actor is controlled by the player. """
        return True

    def be_hit(self, other, history):
        ''' Be brutally battered.
        Args:
            other (Actor): The entity doing the damage.
            history (list<str>): The log.
        '''
        self.health -= 1
        if not self.is_alive():
            self.die(history)

    def die(self, history):
        ''' Be no longer alive.
        Args:
            history (list<str>): The log.
        '''

        self.health = 0
        history.append("You die...")
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
        old_cell.actor = Actor('tail', self.cur_color())
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
        if not target_cell.actor:
            return False # nothing to be hit

        history.append("You devour {}!".format(target_cell.actor.get_the_name()))
        if target_cell.actor._id == 'tail': #XXX: figure out a better way to do this than a literal string comparison
            history[-1] += " (Ouch!)"
            self.be_hit(self, history)
        target_cell.actor = None # XXX: this is killing the actor but will probably need to be generalized at some point
        return True

    def is_alive(self):
        return self.health > 0

    def cur_color(self):
        """ What color is the player at present?
        Returns:
            Color: A color corresponding to the player's health.
        """
        colors = {
            3 : crender.colors.EMERALD,
            2 : crender.colors.YELLOW,
            1 : crender.colors.RED,
            0 : crender.colors.RUST
        }

        return colors.get(self.health, crender.colors.MAGENTA)

    def heal(self, amount):
        ''' (Partially) restore the player's HP, up to the max.
        Args:
            amount (int): The # of HP to restore.
        '''

        self.health = min(self.health + amount, MAX_HP)
