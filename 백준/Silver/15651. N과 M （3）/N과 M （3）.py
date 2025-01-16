def comb(lev):
    global arr, choose, n, m
    if lev == m:
        print(*choose)
        return
    
    for i in range(n):
        choose.append(arr[i])
        comb(lev+1)
        choose.pop()

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
choose = []

comb(0)