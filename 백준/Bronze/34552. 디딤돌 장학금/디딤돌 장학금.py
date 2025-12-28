m = list(map(int, input().split()))
n = int(input())
res = 0

for _ in range(n):
    b, l, s = input().split()
    b = int(b)
    l = float(l)
    s = int(s)
    if l >= 2.0 and s >= 17:
        res += m[b]

print(res)