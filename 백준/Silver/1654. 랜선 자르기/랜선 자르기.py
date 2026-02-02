k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]
result = 0

start = 1
end = max(l)

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for x in l:
        cnt += x // mid

    if cnt < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)