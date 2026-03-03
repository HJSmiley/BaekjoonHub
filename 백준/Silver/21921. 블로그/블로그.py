n, x = map(int, input().split())
visitors = list(map(int, input().split()))

current_sum = sum(visitors[:x])
max_visitors = current_sum
max_count = 1

for i in range(x, n):
    current_sum = current_sum + visitors[i] - visitors[i - x]

    if current_sum > max_visitors:
        max_visitors = current_sum
        max_count = 1
    elif current_sum == max_visitors:
        max_count += 1

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(max_count)