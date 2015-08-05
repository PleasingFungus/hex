''' a simple melee enemy. '''

from actor import Actor
from crender.colors import PURPLE
from point import Point
from rand import coinflip

class Ghost(Actor):
    ''' A simple melee enemy. '''
    def __init__(self):
        super().__init__('ghost', PURPLE)

    def act(self, area, history):
        ''' Take a turn.
        Args:
            area (Area): The area the ghost is in.
            history (list<str>): The log.
        '''

        if not self.move_toward_player(area):
            self.hit_player(area, history)

    def move_toward_player(self, area):
        ''' Attempt to move toward the player.
        Args:
            area (Area): The area the ghost is in.
        '''
        
        player = area.get_player()
        player_loc = area.find_actor(player)
        assert player_loc != None

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        delta = player_loc - cur_loc
        h_delta = Point(int(delta.x / abs(delta.x)) if delta.x else 0, 0)
        v_delta = Point(0, int(delta.y / abs(delta.y)) if delta.y else 0)
        if abs(delta.x) > abs(delta.y) or (abs(delta.x) == abs(delta.y) and coinflip()):
            return self.attempt_move(h_delta, area, None) or self.attempt_move(v_delta, area, None)
        else:
            return self.attempt_move(v_delta, area, None) or self.attempt_move(h_delta, area, None)

        # TODO: switch over to a* but with a different obstruction metric

    def valid_move_destination(self, cell):
        ''' Can this actor move into the given cell?
        Args:
            cell (Cell): The map cell in question.
        Returns:
            bool: Whether this actor can move into this cell, ignoring distance.
        '''
        return not cell.actor


# XXX: deduplicate this with the mongoose version (identical)
    def hit_player(self, area, history):
        ''' Attempt to hit the player, if they're adjacent.
        Args:
            area (Area): The area the ghost is in.
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
            history.append("The ghost hits you!")
            player.be_hit(self, history)
            return True
        return False

