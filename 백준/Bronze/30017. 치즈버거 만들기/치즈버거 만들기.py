ax, bx = map(int, input().split())
a = 1
b = 0
while a < ax and b < bx:
    if a == b + 1:
        a += 1
        b += 1
print(a + b)