n = int(input())
arr = sorted(list(map(int, input().split())))
prefix = [0 for _ in range(n + 1)]

for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

print(sum(prefix))