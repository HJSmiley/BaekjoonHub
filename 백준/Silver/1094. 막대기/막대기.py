import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

x = int(input())
tot = [64]

while tot and sum(tot) > x:
    tmp = heapq.heappop(tot)
    if (sum(tot) + (tmp // 2)) < x:
        heapq.heappush(tot, tmp // 2)
    heapq.heappush(tot, tmp // 2)

print(len(tot))