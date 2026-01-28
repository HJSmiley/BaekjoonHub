def solution(m, n, puddles):
    answer = 0

    new_puddles = []
    for x, y in puddles:
        new_puddles.append([x - 1, y - 1])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        if [i, 0] in new_puddles:
            break
        dp[i][0] = 1

    for j in range(n):
        if [0, j] in new_puddles:
            break
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if [i, j] in new_puddles:
                dp[i][j] = 0
            elif [i - 1, j] in new_puddles:
                dp[i][j] = dp[i][j - 1]
            elif [i, j - 1] in new_puddles:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    answer = dp[m - 1][n - 1] % 1_000_000_007
    return answer