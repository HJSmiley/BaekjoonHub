def rec(idx, lev):
    global arr, d, m
    
    # 종료 조건
    if lev == m:
        print(*d)
        return
    
    # 재귀 조건
    for i in range(0, n):
        if check[i] == True:
            continue

        d.append(arr[i])
        check[i] = True

        rec(i+1, lev+1)

        check[i] = False
        d.pop()


# 3 1
n, m = map(int, input().split())

# [1, 2, 3]
arr = [i for i in range(1, n+1)]
check = [False] * n
d = []

rec(0, 0)