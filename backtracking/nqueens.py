# done
# need to test
# epi 16.2
def is_valid(placement):
    diagonals1 = len(set([x - i for i, x in enumerate(placement)])) == len(placement)
    diagonals2 = len(set([x - i for i, x in enumerate(reversed(placement))])) == len(placement)
    return len(placement) == len(set(placement)) and diagonals1 and diagonals2

def increment_last_queen(placement, last):
    while placement[-1] == last:
        placement.pop()
    placement[-1] += 1

def nqueens(n):
    placement = [0]
    while True:
        if len(placement) == n and is_valid(placement):
            return placement
        if is_valid(placement):
            placement.append(0)
            continue
        elif increment_last_queen(placement, n-1):
            continue
    return placement

print nqueens(8)
