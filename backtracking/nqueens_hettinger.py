import itertools

def is_valid(placement):
    diagonals1 = len(set([x - i for i, x in enumerate(placement)])) == len(placement)
    diagonals2 = len(set([x - i for i, x in enumerate(reversed(placement))])) == len(placement)
    return len(placement) == len(set(placement)) and diagonals1 and diagonals2

def nqueens(n):
    return [placement for placement in itertools.permutations(range(0, n)) if is_valid(placement)]

solution = nqueens(8)
print 'Solutions: ', len(solution)
print solution
