n = int(input())

if n % 2 != 0:
    print(0)
    exit()

dp = [0] * max(5, (n + 1))
dp[2] = 3
dp[4] = 11

for i in range(6, n + 1, 2):
    dp[i] = 4 * dp[i - 2] - dp[i - 4]

print(dp[n])