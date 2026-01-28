def solution(triangle):
    h = len(triangle)

    if h == 1:
        return triangle[0][0]

    dp = [[0] * len(row) for row in triangle]

    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    for i in range(2, h):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
        dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
        for j in range(1, len(triangle[i]) - 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return max(dp[-1])