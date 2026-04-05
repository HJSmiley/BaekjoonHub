n = int(input())
d = [-1] * (n + 1)
d[0] = 0

for i in range(1, n + 1):
    d[i] = d[i - 1] + i * (i + 1) + i * (i + 1) // 2

print(d[n])