yB, mB, dB = map(int, input().split())
yN, mN, dN = map(int, input().split())

if yB == yN:
    a = 0
    b = 1
    c = 0
else:
    b = yN - yB + 1
    c = b - 1
    if mB < mN:
        a = yN - yB
    elif mB > mN:
        a = yN - yB - 1
    else:
        if dB <= dN:
            a = yN - yB
        else:
            a = yN - yB - 1

print(a)
print(b)
print(c)