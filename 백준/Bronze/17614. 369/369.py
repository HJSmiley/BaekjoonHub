n = int(input())
count = 0

for i in range(3, n + 1):
    s = str(i)
    for j in s:
        if int(j) in (3, 6, 9):
            count += 1

print(count)