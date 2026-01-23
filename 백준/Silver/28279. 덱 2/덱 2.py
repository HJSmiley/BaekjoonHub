from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dq = deque()

for _ in range(n):
    ins = list(map(int, input().split()))
    a, b = ins[0], ins[-1]
    if a == 1:
        dq.appendleft(b)
    elif a == 2:
        dq.append(b)
    elif a == 3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif a == 4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif a == 5:
        print(len(dq))
    elif a == 6:
        if dq:
            print(0)
        else:
            print(1)
    elif a == 7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif a == 8:
        if dq:
            print(dq[-1])
        else:
            print(-1)
