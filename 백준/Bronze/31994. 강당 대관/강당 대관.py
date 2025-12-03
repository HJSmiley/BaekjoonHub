max_n = 0
res = ""

for _ in range(7):
    name, n = input().split()
    if int(n) > max_n:
        max_n = int(n)
        res = name

print(res)