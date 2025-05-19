n, m, k = map(int, input().split())

a = n // 2

if a >= m:
    a = m

while n + m - 3 * a < k:
    a -= 1

print(a)