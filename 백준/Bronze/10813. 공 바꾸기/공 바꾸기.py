n, m = map(int, input().split())

lst = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    lst[i], lst[j] = lst[j], lst[i]

print(*lst[1:])