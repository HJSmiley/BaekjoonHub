n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    lst = lst[:i-1] + lst[i-1:j][::-1] + lst[j:]

print(*lst)