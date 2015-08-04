''' Code for handling player abilities in console. '''

from ability import ABIL_JUMP
from cinput.cijump import prompt_jump, JumpInputHandler

class ConsoleAbility(object):
    ''' A representation of a player ability for console UI use.
    Attributes:
        abil (Ability): The state of the ability in question.
    '''
    def __init__(self, abil):
        self.abil = abil

    def hotkey(self):
        ''' What key is pressed to activate this ability, if any?
        Returns:
            str: A hotkey that triggers the ability from the momvement UI.
        '''
        hotkeys = {
            ABIL_JUMP : 'a'
        }
        return hotkeys.get(self.abil.idstr)

    def on_activate(self):
        ''' What happens when the ability is activated?
        Returns:
            func<Player, Area, list<str>: bool>: A callback for the ability.
        '''

        if self.abil.cooldown > 0:
            def activation_fail(_, __, history):
                history.append("{} is unusable for the next {} turn{}!".format(self.abil.name(), self.abil.cooldown,
                                                                               '' if self.abil.cooldown == 1 else 's'))
            return activation_fail

        return {
            ABIL_JUMP : prompt_jump
        }.get(self.abil.idstr)

    def state_change(self):
        ''' What state transition does use of this ability cause?
        If None, remains in the present state (does NOT quit).
        Returns:
            class: A new state, or None.
        ''' 
        if self.abil.cooldown > 0:
            return None

        return {
            ABIL_JUMP : JumpInputHandler
        }.get(self.abil.idstr)
