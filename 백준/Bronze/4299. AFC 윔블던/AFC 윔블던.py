hap, cha = map(int, input().split())

a = (hap + cha) // 2
b = (hap - cha) // 2

if hap < cha:
    print(-1)
else:
    if (hap + cha) % 2 == 0 and (hap - cha) % 2 == 0:
        print(a, b)
    else:
        print(-1)