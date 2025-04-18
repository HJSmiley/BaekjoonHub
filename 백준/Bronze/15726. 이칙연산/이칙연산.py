a, b, c = map(int, input().split())

if b > c:
    print(a*b//c)
else:
    print(a*c//b)