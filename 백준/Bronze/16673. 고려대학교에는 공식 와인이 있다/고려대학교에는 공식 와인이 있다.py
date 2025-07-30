c, k, p = map(int, input().split())
res = 0

if c == 0:
    print(0)
else:
    for i in range(1, c+1):
        res += k * i + p * (i**2)
    print(res)