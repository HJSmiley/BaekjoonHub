from collections import deque

def solution(maps):
    dy = [1, 0, -1, 0]
    dx = [0, -1, 0, 1]

    n, m = len(maps), len(maps[0])
    q = deque()

    q.append((0, 0))

    while q:
        y, x = q.popleft()

        if x == m - 1 and y == n - 1:
            return maps[y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if maps[ny][nx] == 0:
                continue

            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))

    return -1