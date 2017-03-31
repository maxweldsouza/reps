# ctci 16.10
from collections import defaultdict
import operator

def living_people(births, deaths):
    birthdict = defaultdict(int)
    deathdict = defaultdict(int)

    for b in births:
        birthdict[b] += 1
    for d in deaths:
        deathdict[d] += 1

    counts = [0]

    for i in range(1900, 2001):
        counts.append(counts[-1] + birthdict[i] - deathdict[i-1])

    index, _ = max(enumerate(counts), key=operator.itemgetter(1))

    return index - 1 + 1900

print living_people([1900, 1901, 1950], [2001])
