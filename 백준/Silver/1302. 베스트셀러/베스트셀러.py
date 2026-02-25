from collections import defaultdict

dt = defaultdict(int)
n = int(input())

for _ in range(n):
    dt[input()] += 1

dt = sorted(dt.items(), key=lambda x: (-x[1], x[0]))
print(dt[0][0])