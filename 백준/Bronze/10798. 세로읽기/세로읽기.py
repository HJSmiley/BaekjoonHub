lst = [[c for c in input()] for _ in range(5)]
result = []
n = max(len(row) for row in lst)

for i in range(n):
    for j in range(5):
        try:
            result.append(lst[j][i])
        except IndexError:
            pass


print(*result, sep='')