n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)

while start <= end:
    h = (start + end) // 2
    total_h = 0

    for height in heights:
        total_h += max(height - h, 0)

    if total_h >= m:
        answer = h
        start = h + 1
    else:
        end = h - 1

print(answer)