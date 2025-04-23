a, b = map(int, input().split())
c = int(input())

x = a + b
y = 2 * c
if x >= y:
    print(x - y)
else:
    print(x)