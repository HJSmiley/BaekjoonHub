def comb(idx, lev):
    global arr, m
    
    if lev == m:
        print(*choose)
        return
    
    for i in range(idx, n):
        choose.append(arr[i])
        comb(i+1, lev+1)
        choose.pop()

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
choose = []

comb(0, 0)