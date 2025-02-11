arr = [list(map(int, input().split())) for _ in range(9)]
res = arr[0][0]
pos = [0, 0]
for i in range(9):
    for j in range(9):
        if arr[i][j] >= res:
            res = arr[i][j]
            pos[0], pos[1] = i+1, j+1

print(res)
print(*pos)