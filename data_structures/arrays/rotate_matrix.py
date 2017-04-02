# done but need to test
# wont handle rectangular matrices

from itertools import izip

def mid(mx):
    return (mx / 2) - 1 if mx % 2 == 0 else mx / 2

def rotate(mat, w, i, j):
    w -= 1
    mat[i][j], mat[w-j][i], mat[w-i][w-j], mat[j][w-i] = mat[w-j][i], mat[w-i][w-j], mat[j][w-i], mat[i][j]

def rotate_matrix(mat, w):
    m = mid(w)
    for i in range(0, m+1):
        for j in range(i, m+1):
            rotate(mat, w, i, j)
    return mat

test = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]

#print rotate_matrix(test, 3)

# much better method, handles rectanglular matrices
def rotate_iter(mat):
    return map(list, map(reversed, izip(*mat)))

print rotate_iter(test)
