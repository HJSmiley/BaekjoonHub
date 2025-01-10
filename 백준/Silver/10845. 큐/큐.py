import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
q = deque()
n = int(input())

for _ in range(n):
    o = input().split()
    if o[0] == 'push':
        q.append(o[1])
    elif o[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif o[0] == 'size':
        print(len(q))
    elif o[0] == 'empty':
        print(int(bool(not q)))
    elif o[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif o[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])