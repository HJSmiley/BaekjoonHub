from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    dt = defaultdict(list)
    answer = 1

    for _ in range(n):
        # hat headgear
        name, sort = input().split()
        dt[sort].append(name)

    for key in dt:
        answer *= len(dt[key]) + 1

    print(answer - 1)