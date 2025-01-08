import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    order = list(map(int, input().split()))
    if len(order) == 2:
        s.append(order[1])
    elif order[0] == 2:
        if len(s) != 0:
            print(s.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(s))
    elif order[0] == 4:
        if len(s) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(s) != 0:
            print(s[-1])
        else:
            print(-1)