n = int(input())
res = 0

for x in range(1, n + 1):
    flag = True
    for i in range(1, len(str(x)) - 1):
        if int(str(x)[i + 1]) - int(str(x)[i]) != int(str(x)[i]) - int(str(x)[i - 1]):
            flag = False
            break
    if flag:
        res += 1

print(res)