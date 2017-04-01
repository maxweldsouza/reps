# done but ugly
#
import itertools

def right(i, j):
    return i, j + 1

def down(i, j):
    return i - 1, j

def left(i, j):
    return i, j - 1

def up(i, j):
    return i + 1, j

def spiral(arr, w, h):
    dirs = itertools.cycle([right, up, left, down])
    i, j = 0, 0
    total = w * h
    count = 0
    nxt_dir = next(dirs)

    while count < total - 1:
        yield arr[i][j]
        count += 1
        arr[i][j] = None

        ni, nj = nxt_dir(i, j)
        while ni >= w or ni < 0 or nj >= h or nj < 0 or arr[ni][nj] == None:
            print ni, nj
            nxt_dir = next(dirs)
            ni, nj = nxt_dir(i, j)

        i, j = ni, nj

    yield arr[i][j]

test = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
print list(spiral(test, 3, 3))
