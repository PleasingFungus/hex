''' a simple melee enemy. '''

from actor import Actor
from astar import a_star_search
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
        # TODO: deduplicate with mongoose code
        
        player = area.get_player()
        player_loc = area.find_actor(player)
        assert player_loc != None

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        def passable_metric(cell):
            ''' Can the cell be pathed through? '''
            if cell.actor and not cell.actor.is_mobile():
                return False # don't path through fixed creatures
            return True

        # attempt to move toward the player
        path = a_star_search(area.cells, cur_loc, player_loc, passable_metric)
        # TODO: improve performance when the player is unreachable
        if path:
            return self.attempt_move(path[0] - cur_loc, area, None)

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

