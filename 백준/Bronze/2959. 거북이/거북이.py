from itertools import permutations

a, b, c, d = map(int, input().split())
lengths = list(permutations([a, b, c, d]))
max_area = 0

for l in lengths:
    if l[0] >= l[2] and l[1] <= l[3]:
        max_area = max(max_area, l[1] * l[2])

print(max_area)