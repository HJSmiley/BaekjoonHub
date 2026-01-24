from itertools import product


def solution(N, number):
    if number == N:
        return 1
    elif number in [1, 2 * N, 11 * N, N**2]:
        return 2
    
    dp = [[] for _ in range(9)]
    dp[1] = [N]
    dp[2] = [1, 2 * N, 11 * N, N**2]

    for i in range(3, 9):
        dp[i].append(N * sum([10**k for k in range(i)]))
        for j in range(1, i):
            dp[i] += [x + y for x, y in product(dp[j], dp[i - j])]
            dp[i] += [x - y for x, y in product(dp[j], dp[i - j])]
            dp[i] += [x * y for x, y in product(dp[j], dp[i - j])]
            dp[i] += [x // y for x, y in product(dp[j], dp[i - j]) if y != 0]

            if number in set(dp[i]):
                return i

    return -1