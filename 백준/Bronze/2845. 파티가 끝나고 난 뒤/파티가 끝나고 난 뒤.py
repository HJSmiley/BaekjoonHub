l, p = map(int, input().split())
cnt = list(map(int, input().split()))

ans = l * p

for i in cnt:
    print(i - ans, end=' ')