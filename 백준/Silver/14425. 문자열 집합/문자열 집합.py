n, m = map(int, input().split())
dict = {}
ans = 0

for _ in range(n):
    s = input()
    dict[s] = True

for _ in range(m):
    s = input()
    if s in dict:
        ans += 1

print(ans)