''' Functions for randomness. '''

from random import seed, randrange, randint, choice

def random2(x):
    ''' Return a random number in [0,x). '''
    if x <= 0:
        return 0
    return randint(0, x-1)

def random_choose_weighted(*options):
    ''' Choose a random option from a weighted list.
    Adapted from crawl's implementation: https://github.com/crawl/crawl/commit/5c15e6abda97c .
    Args:
        options (list<tuple<int, object>>): A list of weights and corresponding objects.
        The chance of any given item being chosen is its weight / the sum of all item weights.
    Returns:
        object: A chosen object from the list.
    '''
    total_weight = sum(weight for weight, option in options)
    r = random2(total_weight)

    seen_weight = 0
    for weight, option in options:
        seen_weight += weight
        if seen_weight > r:
            return option
    return None
