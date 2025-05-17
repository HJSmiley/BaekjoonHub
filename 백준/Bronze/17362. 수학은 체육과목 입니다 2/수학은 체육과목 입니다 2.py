n = int(input())
d = n % 8

if d == 1:
    print(1)
elif d == 2 or d == 0:
    print(2)
elif d == 3 or d == 7:
    print(3)
elif d == 4 or d == 6:
    print(4)
elif d == 5:
    print(5)