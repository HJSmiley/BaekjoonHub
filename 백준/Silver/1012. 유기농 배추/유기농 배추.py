from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]
    num = 0

    for _ in range(k):
        a, b = map(int, input().split())
        maps[b][a] = 1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                q = deque()
                q.append((i, j))
                maps[i][j] = 0
                num += 1

                while q:
                    y, x = q.popleft()

                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]

                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue

                        if maps[ny][nx] == 0:
                            continue

                        if maps[ny][nx] == 1:
                            maps[ny][nx] = 0
                            q.append((ny, nx))

    print(num)