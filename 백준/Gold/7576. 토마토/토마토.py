from collections import deque

m, n = map(int, input().split())
arr = []
q = deque()

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(m):
        if row[j] == 1:
            q.append((i, j))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x] + 1
                q.append((ny, nx))

bfs()

def get_day():
    ans = 0
    for row in arr:
        if 0 in row:
            return -1

        row_max = max(row)
        if ans < row_max:
            ans = row_max
    return ans - 1

print(get_day())