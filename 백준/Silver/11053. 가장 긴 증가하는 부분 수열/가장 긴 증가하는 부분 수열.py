n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
answer = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[j] + 1, d[i])

print(max(d))