''' a simple melee enemy. '''

from actor import Actor
from astar import a_star_search
from crender.colors import RUST

class Mongoose(Actor):
    ''' A simple melee enemy. '''
    def __init__(self):
        super().__init__('o', RUST)
        self.is_mobile = True
        self.is_hittable = True

    def act(self, area):
        ''' Take a turn.
        Args:
            area (Area): The area the mongoose is in.
        '''

        self.move_toward_player(area)
        if not self.hit_player(area):
            self.move_toward_player(area)

    def move_toward_player(self, area):
        ''' Attempt to move toward the player.
        Args:
            area (Area): The area the mongoose is in.
        '''
        
        player = area.get_player()
        player_loc = area.find_actor(player)
        assert player_loc != None

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        # attempt to move toward the player
        path = a_star_search(area.cells, cur_loc, player_loc)
        if path:
            self.attempt_move(path[0] - cur_loc, area)
            return

        # XXX: just move directly toward the player

    def hit_player(self, area):
        ''' Attempt to hit the player, if they're adjacent.
        Args:
            area (Area): The area the mongoose is in.
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
            player.be_hit(self)
            return True
        return False

