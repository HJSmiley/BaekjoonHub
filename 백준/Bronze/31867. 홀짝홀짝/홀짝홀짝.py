n = int(input())
k = input()
res = 0

for num in k:
    if int(num) % 2 == 0:
        res += 1
    else:
        res -= 1

if res > 0:
    print(0)
elif res < 0:
    print(1)
else:
    print(-1)