def pooling(matrix, x, y, N):
    if N == 1:
        return matrix[x][y]

    half = N // 2

    sect1 = pooling(matrix, x, y, half)
    sect2 = pooling(matrix, x, y + half, half)
    sect3 = pooling(matrix, x + half, y, half)
    sect4 = pooling(matrix, x + half, y + half, half)

    tmp = sorted([sect1, sect2, sect3, sect4], reverse=True)

    return tmp[1]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

print(pooling(lst, 0, 0, n))