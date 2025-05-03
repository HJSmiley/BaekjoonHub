n, m = map(int, input().split())

lst = [0 for _ in range(n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i, j+1):
        lst[a] = k

print(*lst[1:])