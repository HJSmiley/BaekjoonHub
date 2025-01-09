n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]
arr = sorted(arr, key = lambda x: int(x[0]))

for i in arr:
    print(i[0], i[1])