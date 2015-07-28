''' Functions for randomness. '''

from random import seed, randrange, randint, choice

seed(27) # eh

def random2(x):
    ''' Return a random number in [0,x). '''
    if x <= 0:
        return 0
    return randint(0, x-1)
