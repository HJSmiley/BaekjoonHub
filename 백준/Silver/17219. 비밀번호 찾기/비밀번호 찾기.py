n, m = map(int, input().split())
dt = {}

for _ in range(n):
    site, pw = input().split()
    dt[site] = pw

for _ in range(m):
    print(dt[input()])