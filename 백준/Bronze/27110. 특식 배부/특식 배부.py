n = int(input())
a, b, c = map(int, input().split())
result = 0

for i in (a, b, c):
    if i <= n:
        result += i
    else:
        result += n

print(result)