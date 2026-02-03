def sol(houses):
    n = len(houses)

    houses = [0] + houses
    dp = [0] * (n + 1)

    dp[1] = houses[1]
    dp[2] = max(houses[1], houses[2])

    for i in range(3, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    return dp[n]

def solution(money):
    return max(sol(money[:-1]), sol(money[1:]))