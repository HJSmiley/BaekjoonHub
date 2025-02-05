pcs = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
result = []

for i in range(6):
    result.append(pcs[i] - arr[i])
print(*result)