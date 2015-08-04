''' Code for handling player abilities in console. '''

from ability import ABIL_JUMP
from cinput.cijump import prompt_jump, JumpInputHandler

class ConsoleAbility(object):
    ''' A representation of a player ability for console UI use.
    Attributes:
        idstr (str): A unique identifying string for the ability.'''
    def __init__(self, idstr):
        self.idstr = idstr

    def hotkey(self):
        ''' What key is pressed to activate this ability, if any?
        Returns:
            str: A hotkey that triggers the ability from the momvement UI.
        '''
        hotkeys = {
            ABIL_JUMP : 'a'
        }
        return hotkeys.get(self.idstr)

    def on_activate(self):
        ''' What happens when the ability is activated?
        Returns:
            func<Player, Area, list<str>: bool>: A callback for the ability.
        '''
        return {
            ABIL_JUMP : prompt_jump
        }.get(self.idstr)

    def state_change(self):
        ''' What state transition does use of this ability cause?
        If None, remains in the present state (does NOT quit).
        Returns:
            class: A new state, or None.
        ''' 
        return {
            ABIL_JUMP : JumpInputHandler
        }.get(self.idstr)
