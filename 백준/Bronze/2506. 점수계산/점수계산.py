n = int(input())
scores = list(map(int, input().split()))
flag = 0
total = 0

for score in scores:
    if score == 0:
        flag = 0
        continue
    elif score == 1 and flag:
        total += (flag + 1)
        flag += 1
    else:
        total += 1
        flag += 1

print(total)