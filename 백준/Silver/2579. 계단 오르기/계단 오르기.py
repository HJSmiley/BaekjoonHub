n = int(input())
s = [int(input()) for _ in range(n)]

if n == 1:
    print(s[0])
elif n == 2:
    print(s[0] + s[1])
else:
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[0] + s[2], s[1] + s[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + s[i], dp[i - 3] + s[i - 1] + s[i])

    print(dp[n - 1])