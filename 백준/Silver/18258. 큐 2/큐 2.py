import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

q = deque()

n = int(input())

for _ in range(n):
    o = input()

    if o == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif o == 'size':
        print(len(q))
    elif o == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif o == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif o == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        o = o.split()
        q.append(o[1])