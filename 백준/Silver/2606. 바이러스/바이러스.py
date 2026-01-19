from collections import deque

n = int(input())
t = int(input())

visited = [False] * (n + 1)
adj_lst = [[] for _ in range(n + 1)]
q = deque()
result = 0

for _ in range(t):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

q.append(1)
visited[1] = True

while q:
    node = q.popleft()

    for adj_node in adj_lst[node]:
        if visited[adj_node]:
            continue
        q.append(adj_node)
        visited[adj_node] = True
        result += 1

print(result)