import math

a, b, c = map(int, input().split())

if b == c:
    print(-1)
else:
    n = int(a / (c - b) + 1)
    print(max(n, -1))