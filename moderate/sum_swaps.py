# ctci 16.21

from collections import defaultdict

def sum_swaps(a, b):
    sa, sb = sum(a), sum(b)
    if (sa - sb) % 2 != 0:
        return None
    target = (sa - sb) / 2
    db = defaultdict(bool)
    for y in b:
        db[y] = True
    for x in a:
        if x - target in db:
            return (x, x-target)
    return None

print sum_swaps([4, 1, 2, 1, 1, 2], [3, 6, 3, 3])
