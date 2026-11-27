n = int(input())
lev = n // 2 + 1

if n % 2 == 0:
    print(lev**2)
else:
    print(lev**2 + lev)