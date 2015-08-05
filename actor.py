''' Actor class & methods. '''

import json

import crender.colors

class Actor(object):
    ''' An entity that occupies a Cell.
        Attributes:
            _id (str): The id of the actor type.
            color (Color): The color of the actor.
    '''
    def __init__(self, _id, color):
        if _id not in actor_data:
            raise ValueError("Unknown actor ID {}!".format(_id))
        self._id = _id
        self.color = color

    def is_player(self):
        ''' Is this actor controlled by the player? '''
        return False

    def actor_data(self, key):
        ''' Get the raw actor data value corresponding to this actor. '''
        return actor_data[self._id][key]

    def is_mobile(self):
        ''' Is this actor capable of movement? (Or should it be treated as stationary
        for e.g. pathfinding purposes?'''
        return self.actor_data('mobile')

    def get_the_name(self):
        ''' 'the mongoose' or 'your tail' '''
        return self.actor_data('the_name')

    def cur_glyph(self):
        ''' What glyph should currently be used to represent this actor in the console?
        Returns:
            str: The correct glyph for the actor; e.g. '@'.
        '''
        return self.actor_data('glyph')

    def cur_color(self):
        ''' What color should currently be used for this actor's glyph in the console?
        Returns:
            Color: The correct color for the actor.
        '''
        return self.color

    def act(self, area, history):
        ''' Take a turn.
        args:
            area (Area): The area the actor is in.
            history (list<str>): The log.
        '''
        pass

    def attempt_move(self, delta, area, history):
        ''' Attempt to move the actor the given delta from their current position in the current area.

        Args:
            delta (Point): The delta to move from the actor's current position.
            area (Area): The area the actor is in.
            history (list<str>): The log.
        Returns:
            bool: Whether the actor successfully moved.
        '''

        cur_loc = area.find_actor(self)
        assert cur_loc != None

        new_loc = cur_loc + delta
        if new_loc not in area.cells: # OOB
            return False

        new_cell = area.cells[new_loc]
        if not self.valid_move_destination(new_cell):
            return False

        # let's move!
        cur_cell = area.cells[cur_loc]
        assert cur_cell
        cur_cell.actor = None
        new_cell.actor = self
        return True

    def valid_move_destination(self, cell):
        ''' Can this actor move into the given cell?
        Args:
            cell (Cell): The map cell in question.
        Returns:
            bool: Whether this actor can move into this cell, ignoring distance.
        '''
        return not cell.is_full()

def validate(actor_data):
    ''' Check to make sure that the data actually matches our schema. '''
    schema = { 'mobile' : bool, 'the_name' : str, 'glyph' : str }
    for _id, data in actor_data.items():
        for key, stype in schema.items():
            if key not in data:
                raise ValueError("Mandatory field {} not present in {}!".format(key, _id))
            dtype = type(data[key])
            if dtype != stype:
                raise ValueError("Field {} has incorrect type {} (instead of {}) in {}!".format(key, dtype, stype, _id))
        for key in data:
            if key not in schema:
                raise ValueError("Unknown field {} in {}!".format(key, _id))

actor_data = {}
with open('data/actors.json') as f:
    actor_data.update(json.load(f))
    validate(actor_data)

