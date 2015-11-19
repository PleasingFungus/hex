''' a simple melee enemy. '''

from actor import Actor
from astar import a_star_search
from crender.colors import RUST

MOVES_PER_TURN = 2

class Mongoose(Actor):
    ''' A simple melee enemy. '''
    def __init__(self):
        super().__init__('mongoose', RUST)
        self.moves_taken = 0

    def act(self, area, history):
        ''' Take a turn.
        Args:
            area (Area): The area the mongoose is in.
            history (list<str>): The log.
        Returns:
            bool: Whether the mongoose is done for the turn (True),
                  or whether it wants to take more actions (False).
        '''

        if self.hit_player(area, history):
            return True

        moved = self.move_toward_player(area)
        if not moved:
            return False

        self.moves_taken += 1
        return self.moves_taken >= MOVES_PER_TURN

    def move_toward_player(self, area):
        ''' Attempt to move toward the player.
        Args:
            area (Area): The area the mongoose is in.
        Returns:
            bool: Whether the mongoose moved.
        '''
        
        player = area.get_player()
        player_loc = area.find_actor(player)
        assert player_loc != None

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        def passable_metric(cell):
            ''' Can the cell be pathed through? '''
            if cell.solid:
                return False # don't path through walls
            if cell.actor and not cell.actor.is_mobile():
                return False # don't path through fixed creatures
            return True

        # attempt to move toward the player
        path = a_star_search(area.cells, cur_loc, player_loc, passable_metric)
        # TODO: improve performance when the player is unreachable
        if path:
            self.attempt_move(path[0] - cur_loc, area, None)
            return True
        return False

        # XXX: just move directly toward the player

    def hit_player(self, area, history):
        ''' Attempt to hit the player, if they're adjacent.
        Args:
            area (Area): The area the mongoose is in.
            history (list<str>): The log.
        Returns:
            Whether the player was in range to be hit.
        '''

        player = area.get_player()
        player_loc = area.find_actor(player)
        assert player_loc != None

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        # attempt to hit the player
        if player_loc.adjacent(cur_loc):
            history.append("The mongoose hits you!")
            player.be_hit(self, history)
            return True
        return False

    def end_of_turn_cleanup(self):
        ''' Reset moves_taken at EOT. '''
        self.moves_taken = 0
