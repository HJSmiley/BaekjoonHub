n = int(input())
v1 = [0] * n
v2 = [0] * (2 * n - 1)
v3 = [0] * (2 * n - 1)
answer = 0

def dfs(i):
    global answer

    if i == n:
        answer += 1
        return

    for j in range(n):
        if v1[j] == v2[i + j] == v3[i - j] == 0:
            v1[j] = v2[i + j] = v3[i - j] = 1
            dfs(i + 1)
            v1[j] = v2[i + j] = v3[i - j] = 0

    return

dfs(0)
print(answer)