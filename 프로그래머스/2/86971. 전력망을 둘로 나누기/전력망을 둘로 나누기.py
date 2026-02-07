from collections import deque

def solution(n, wires):
    answer = n

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        cnt = 1
        visited = [False] * (n + 1)
        visited[a] = True
        q = deque([a])

        while q:
            curr = q.popleft()
            for nxt in graph[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    cnt += 1

        answer = min(answer, abs(cnt - (n - cnt)))

        graph[a].append(b)
        graph[b].append(a)

    return answer