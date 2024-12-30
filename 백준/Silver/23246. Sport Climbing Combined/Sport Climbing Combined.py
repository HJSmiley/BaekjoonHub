N = int(input())
lsts = [tuple(map(int, input().split())) for _ in range(N)]
arr = []

for lst in lsts:
    arr.append([lst[1] * lst[2] * lst[3], lst[1] + lst[2] + lst[3], lst[0]])
    arr = sorted(arr)

print(arr[0][2], arr[1][2], arr[2][2])