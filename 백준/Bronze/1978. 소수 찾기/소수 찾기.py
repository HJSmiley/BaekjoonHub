n = int(input())
arr = list(map(int, input().split()))

d = [True] * (max(arr)+1)
d[0] = d[1] = False

for i in range(2, int(max(arr)**0.5)+1):
    if not d[i]:
        continue
    for j in range(2*i, max(arr)+1, i):
        d[j] = False

ans = [d[i] for i in arr]

print(sum(ans))