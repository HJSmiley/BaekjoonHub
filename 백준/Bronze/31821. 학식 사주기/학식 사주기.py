res = 0

n = int(input())
a = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    a[i] = int(input())

m = int(input())
for j in range(m):
    res += a[int(input())]

print(res)