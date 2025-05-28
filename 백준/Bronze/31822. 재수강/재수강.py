sub = input()[:5]
n = int(input())
res = 0

for _ in range(n):
    sugang = input()[:5]
    if sub == sugang:
        res += 1

print(res)