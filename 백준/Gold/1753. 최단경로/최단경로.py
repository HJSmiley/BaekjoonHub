import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

INF = int(1e12)
V, E = map(int, input().split())
K = int(input())

adj_lst = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_lst[u].append([v, w])

dist = [INF] * (V + 1)
dist[K] = 0
hq = []
heapq.heappush(hq, [0, K])

while hq:
    cur_dist, cur_node = heapq.heappop(hq)

    if cur_dist > dist[cur_node]:
        continue

    for adj_node, adj_dist in adj_lst[cur_node]:
        temp_dist = cur_dist + adj_dist
        if temp_dist < dist[adj_node]:
            heapq.heappush(hq, [temp_dist, adj_node])
            dist[adj_node] = temp_dist

for i in range(1, V + 1):
    print("INF" if dist[i] == INF else dist[i])