import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = []

for _ in range(n):
    o = input()
    if 'push' in o:
        o, x = o.split()
        s.append(x)
    elif o == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif o == 'size':
        print(len(s))
    elif o == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])