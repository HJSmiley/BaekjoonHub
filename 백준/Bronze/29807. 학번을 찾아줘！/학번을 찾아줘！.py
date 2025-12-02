t = int(input())
lst = list(map(int, input().split()))

while len(lst) <= 5:
    lst.append(0)

if lst[0] > lst[2]:
    x = (lst[0] - lst[2]) * 508
else:
    x = (lst[2] - lst[0]) * 108

if lst[1] > lst[3]:
    y = (lst[1] - lst[3]) * 212
else:
    y = (lst[3] - lst[1]) * 305

if lst[4]:
    z = lst[4] * 707
else:
    z = 0

print((x + y + z) * 4763)