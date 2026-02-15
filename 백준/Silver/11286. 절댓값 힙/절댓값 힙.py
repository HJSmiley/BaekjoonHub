import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
hq = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            _, ans = heapq.heappop(hq)
            print(ans)
        else:
            print(0)