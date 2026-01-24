from collections import deque

n = int(input())
dq = deque([i for i in range(1, n + 1)])
pn = [0] + list(map(int, input().split()))
res = []

while dq:
    tmp = dq.popleft()
    k = pn[tmp]
    if dq:
        if k > 0:
            for _ in range(k - 1):
                dq.append(dq.popleft())
        else:
            for _ in range(-k):
                dq.appendleft(dq.pop())
    res.append(tmp)

print(*res)