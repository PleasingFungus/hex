''' a simple melee enemy. '''

from actor import Actor
from astar import a_star_search
from crender.colors import RUST

class Mongoose(Actor):
    ''' A simple melee enemy. '''
    def __init__(self):
        super().__init__('o', RUST)
        self.is_mobile = True

    def act(self, area):
        ''' Take a turn.
        args:
            area (Area): The area the actor is in.
        '''
        cur_loc = area.find_actor(self)
        assert cur_loc != None

        for actor in area.all_actors():
            if actor.is_player:
                player = actor
        assert player

        player_loc = area.find_actor(player)
        assert player_loc != None

        # attempt to hit the player
        if player_loc.adjacent(cur_loc):
            player.be_hit(self)
            return

        # attempt to move toward the player
        path = a_star_search(area.cells, cur_loc, player_loc)
        if path:
            self.attempt_move(path[0] - cur_loc, area)
            return

        # XXX: just move directly toward the player
