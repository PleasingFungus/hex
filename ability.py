""" Player abilities. """

class Ability(object):
    ''' A player ability & its state.
    Attributes:
        idstr (str): A unique identifier for the ability.
        cooldown (int): Remaining turns unti the ability can be used.
    '''
    
    def __init__(self, idstr, cooldown=0):
        self.idstr = idstr
        self.cooldown = cooldown

    def name(self):
        return names[self.idstr]

ABIL_JUMP = "jump"

names = {
    ABIL_JUMP : "Jump"
}
