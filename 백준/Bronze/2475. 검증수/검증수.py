num = list(map(int, input().split()))
unum = 0
for i in num:
    unum += i**2
unum %= 10
print(unum)