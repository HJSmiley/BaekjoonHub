from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
q = deque([(n, 0)])
visited[n] = True

while q:
    x, time = q.popleft()

    if x == k:
        print(time)
        break

    for i in (x - 1, x + 1, 2 * x):
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = True
            q.append((i, time + 1))