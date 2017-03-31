# ctci 16.15
#done

from itertools import izip

def master_mind(solution, guess):
    hits = 0
    allhits = 0
    for s, g in izip(solution, guess):
        if s == g:
            hits += 1
    for x in 'RYGB':
        counts = sum([1 for i in solution if i == x])
        countg = sum([1 for i in guess if i == x])
        allhits += min(counts, countg)
    return (hits, allhits - hits)

assert master_mind('RGBY', 'GGRR') == (1, 1)
assert master_mind('RGBY', 'RGBY') == (4, 0)
assert master_mind('RRRR', 'RRRR') == (4, 0)
assert master_mind('RRRR', 'BBBB') == (0, 0)
assert master_mind('RRBB', 'BBRR') == (0, 4)
