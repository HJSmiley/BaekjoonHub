n = int(input())
d = [[0] * 10 for _ in range(n+1)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for N in range(2, n+1):
    d[N][0] = d[N-1][1]
    d[N][9] = d[N-1][8]

    for K in range(1, 9):
        d[N][K] = d[N-1][K-1] + d[N-1][K+1]

print(sum(d[n])%1000000000)