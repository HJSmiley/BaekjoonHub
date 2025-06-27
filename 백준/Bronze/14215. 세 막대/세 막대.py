a, b, c = sorted(map(int, input().split()))

while (a + b <= c):
    c -= 1
    a, b, c = sorted([a, b, c])

print(a+b+c)