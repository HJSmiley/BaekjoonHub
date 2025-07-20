t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    u = 2 * m - n
    t = m - u
    print(u, t)