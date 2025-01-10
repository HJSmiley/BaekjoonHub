t = int(input())

for _ in range(t):
    dic = {0: 0, 1: 0}
    lst = list(input())
    for i in lst:
        if i == '(':
            dic[0] += 1
        if i == ')':
            dic[1] += 1
        if dic[0] != 0 and dic[1] != 0 and dic[0] == dic[1]:
            dic[0] = 0
            dic[1] = 0
        if dic[1] > dic[0]:
            break
    if dic[0] == 0 and dic[1] == 0:
        print('YES')
    else:
        print('NO')