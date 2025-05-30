x0, n = map(int, input().split())
x = [-1 for _ in range(n+1)]
x[0] = x0

for i in range(n):
    if x[i] % 2 == 0:
        x[i+1] = (x[i] // 2) ^ 6
    else:
        x[i+1] = (2 * x[i]) ^ 6

print(x[n])