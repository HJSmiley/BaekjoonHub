import heapq

def solution(n, costs):
    adj_lst = [[] for _ in range(n)]
    for c in costs:
        adj_lst[c[0]].append([c[1], c[2]])
        adj_lst[c[1]].append([c[0], c[2]])

    hq = [[0, 0]]
    visited = [False] * n
    total_cost = 0
    connected_count = 0

    while hq:
        cost, node = heapq.heappop(hq)

        if visited[node]:
            continue

        visited[node] = True
        total_cost += cost
        connected_count += 1

        if connected_count == n:
            break

        for next_node, next_cost in adj_lst[node]:
            if not visited[next_node]:
                heapq.heappush(hq, [next_cost, next_node])

    return total_cost