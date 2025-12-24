n = int(input())
res = 0

for _ in range(n):
    s, c, a, r = map(int, input().split())
    if s >= 1000 or c >= 1600 or a >= 1500 or 0 < r <= 30:
        res += 1

print(res)