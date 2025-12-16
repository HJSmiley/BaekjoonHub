n, m, a, b = map(int, input().split())

if (3 * n) > m:
    print((3 * n - m) * a + b)
else:
    print(0)