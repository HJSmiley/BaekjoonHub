from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 1))
visited[0][0] = True

while q:
    i, j, dist = q.popleft()

    # 도착
    if i == n - 1 and j == m - 1:
        print(dist)
        break

    # 상
    if i - 1 >= 0 and maze[i - 1][j] == 1 and not visited[i - 1][j]:
        visited[i - 1][j] = True
        q.append((i - 1, j, dist + 1))

    # 우
    if j + 1 < m and maze[i][j + 1] == 1 and not visited[i][j + 1]:
        visited[i][j + 1] = True
        q.append((i, j + 1, dist + 1))

    # 하
    if i + 1 < n and maze[i + 1][j] == 1 and not visited[i + 1][j]:
        visited[i + 1][j] = True
        q.append((i + 1, j, dist + 1))

    # 좌
    if j - 1 >= 0 and maze[i][j - 1] == 1 and not visited[i][j - 1]:
        visited[i][j - 1] = True
        q.append((i, j - 1, dist + 1))