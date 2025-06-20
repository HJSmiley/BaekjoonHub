t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    y = str(h if n % h == 0 else (n % h))
    x = n // h if n % h == 0 else n // h + 1
    x = str(x) if x >= 10 else '0' + str(x)
    print(y+x)