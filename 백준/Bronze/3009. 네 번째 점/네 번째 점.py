X = []
Y = []
ans = [0, 0]

for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        ans[0] = X[i]
    if Y.count(Y[i]) == 1:
        ans[1] = Y[i]

print(*ans)