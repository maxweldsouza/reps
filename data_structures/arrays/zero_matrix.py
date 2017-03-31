# ctci 1.8
#done

def zeros(matrix, M, N):
    rows = [False for x in range(M)]
    cols = [False for y in range(N)]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(M):
        for j in range(N):
            if rows[i] or cols[j]:
                matrix[i][j] = 0
    return matrix

print zeros([[1,2,3],[0,5,6],[7,8,9]], 3, 3)
