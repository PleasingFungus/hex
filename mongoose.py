''' a simple melee enemy. '''

from actor import Actor
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

        for loc,cell in area.cells.items():
            if not loc.adjacent(cur_loc):
                continue

            if cell.actor and cell.actor.is_player:
                cell.actor.be_hit(self)
                break
