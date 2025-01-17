n = int(input())

cnt2 = 0
cnt5 = 0

for i in range(2, n+1):
    temp = i
    while temp % 2 == 0:
        cnt2 += 1
        temp //= 2
    while temp % 5 == 0:
        cnt5 += 1
        temp //= 5

print(min(cnt2, cnt5))