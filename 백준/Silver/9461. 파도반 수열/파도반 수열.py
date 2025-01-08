import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    p = [0] * 101
    init = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(10):
        p[i+1] = init[i]

    if n > 10:
        for j in range(11, n+1):
            p[j] = p[j-1] + p[j-5]

    print(p[n])