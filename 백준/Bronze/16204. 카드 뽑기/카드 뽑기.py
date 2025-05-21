n, m, k = map(int, input().split())

if m >= k:
    a = k
    b = n-m
else:
    a = m
    b = n-k

print(a+b)