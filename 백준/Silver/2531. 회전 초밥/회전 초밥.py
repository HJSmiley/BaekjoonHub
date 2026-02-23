from collections import defaultdict

n, d, k, c = map(int, input().split())
belts = [int(input()) for _ in range(n)]

belts.extend(belts[: k - 1])

visited = defaultdict(int)
visited[c] += 1

cnt = 1

for i in range(k):
    if visited[belts[i]] == 0:
        cnt += 1
    visited[belts[i]] += 1

max_cnt = cnt

for j in range(n - 1):
    left = belts[j]
    visited[left] -= 1
    if visited[left] == 0:
        cnt -= 1

    right = belts[j + k]
    if visited[right] == 0:
        cnt += 1
    visited[right] += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)