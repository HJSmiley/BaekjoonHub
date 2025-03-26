from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

visited_d = [False for _ in range(n+1)]
visited_b = [False for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()

dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)