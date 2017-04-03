# test and works for simple sudoku
# http://norvig.com/sudoku.html

def next_move(mat, moves):
    w = len(mat)
    for i in range(w):
        for j in range(w):
            if not mat[i][j]:
                moves.append((i, j, 1))
                mat[i][j] = 1
                return

def increment_move(mat, moves):
    while moves[-1][2] == 9:
        if len(moves) == 0:
            return False
        i, j, val = moves.pop()
        mat[i][j] = 0
    i, j, val = moves.pop()
    moves.append((i, j, val+1))
    mat[i][j] = val + 1

def done(mat):
    w = len(mat)
    return all([ mat[i][j] for i in range(w) for j in range(w) ])

def check_row(mat, i):
    assigned = [x for x in mat[i] if x ]
    return len(set(assigned)) == len(assigned)

def check_col(mat, j):
    assigned = [row[j] for row in mat if row[j] ]
    return len(set(assigned)) == len(assigned)

def sub_array(i):
    sub = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    return [s for s in sub if i in s][0]

def check_subarray(mat, i, j):
    assigned = [ mat[x][y] for x in sub_array(i) for y in sub_array(j) if mat[x][y] ]
    return len(set(assigned)) == len(assigned)

def is_valid_move(mat, moves):
    if len(moves) == 0:
        return True
    i, j, value = moves[-1]
    return check_row(mat, i) and check_col(mat, j) and check_subarray(mat, i, j)

def solver(mat):
    moves = [] # every move is a tuple (i, j, value)
    while True:
        if done(mat) and is_valid_move(mat, moves):
            return mat
        if is_valid_move(mat, moves):
            next_move(mat, moves)
        elif increment_move(mat, moves):
            continue
        else:
            return False # unsolvable
    return mat

def string_to_mat(s):
    return [ [int(c) for c in line] for line in s.splitlines() ]

impossible = """000005080
000601043
000000000
010500000
000106000
300000005
530000061
000000004
000000000"""

test = """003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300"""

print solver(string_to_mat(impossible))
