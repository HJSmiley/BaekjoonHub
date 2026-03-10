n, k = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

def recur(idx, cur_w):
    if idx == n:
        return 0

    if dp[idx][cur_w] != -1:
        return dp[idx][cur_w]

    w = goods[idx][0]
    v = goods[idx][1]

    max_v = recur(idx + 1, cur_w)

    if cur_w >= w:
        max_v = max(max_v, v + recur(idx + 1, cur_w - w))

    dp[idx][cur_w] = max_v
    return dp[idx][cur_w]

print(recur(0, k))