from itertools import combinations

heights = [int(input()) for _ in range(9)]
idx = list(combinations(range(9), 7))
answer = []

for i in idx:
    tot = 0
    for j in i:
        tot += heights[j]
    if tot == 100:
        for k in i:
            answer.append(heights[k])
        print(*sorted(answer), sep="\n")
        break