n, a, b = map(int, input().split())
x = y = 1

for _ in range(n):
    x += a
    y += b

    if x < y:
        x, y = y, x
    elif x == y:
        y -= 1

print(x, y)