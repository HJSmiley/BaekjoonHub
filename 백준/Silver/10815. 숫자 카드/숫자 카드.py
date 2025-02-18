n = int(input())
temp = list(map(int, input().split()))
dt = {}

for i in temp:
    dt[i] = -1

m = int(input())
temp = list(map(int, input().split()))
result = [0 for _ in range(m)]

for j in range(m):
    if temp[j] in dt:
        result[j] = 1

print(*result)