# possibly works
# not run

def possible_paths(i, j):
    return [(i-1, j), (i-1, j-1), (i, j-1)]

def valid_square(pos):
    i, j = pos
    return i >= 0 and j >= 0

def min_cost_path(mat, w, h, x, y):
    result = mat.clone()
    for i in range(w):
        for j in range(h):
            result[i][j] = min([mat[pos[0]][pos[1]] for pos in possible_paths(i,j) if valid_square(pos)])
    return result[x][y]
