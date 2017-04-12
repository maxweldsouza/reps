# TODO incomplete
def valid_moves(move):
    i, j = move
    return [
        (i+2, j+1),
        (i+2, j-1),
        (i-2, j+1),
        (i-2, j-1),
        (i+1, j+2),
        (i+1, j-2),
        (i-1, j+2),
        (i-1, j-2),
    ]

def is_valid(solution):
    i, j = solution[-1]
    return 0 <= i < 8 and 0 <= j < 8 and len(set(solution)) == len(solution)

def next_move(move):
    return valid_moves(move)[0]

def backtrack(solution):
    print 'backtracking'
    while not is_valid(solution):
        old = solution.pop()
        print solution[-1]
        valid = valid_moves(solution[-1])
        index = valid.index(old)
        if index < len(valid) - 1:
            solution.append(valid[index + 1])
        else:
            solution.pop()
    return

def knights_tour():
    solution = [(0, 0)]
    while not len(solution) == 64:
        print 'moving ahead'
        print solution[-1]
        if is_valid(solution):
            solution.append(next_move(solution[-1]))
        else:
            backtrack(solution)
    return solution

print knights_tour()
