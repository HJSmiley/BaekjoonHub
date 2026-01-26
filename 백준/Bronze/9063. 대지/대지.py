n = int(input())
lst = [[], []]

for _ in range(n):
    x, y = map(int, input().split())
    lst[0].append(x)
    lst[1].append(y)

print((max(lst[0]) - min(lst[0])) * (max(lst[1]) - min(lst[1])))