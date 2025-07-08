n = int(input())
c_score = s_score = 100

for _ in range(n):
    c, s = map(int, input().split())
    if c > s:
        s_score -= c
    elif s > c:
        c_score -= s

print(c_score)
print(s_score)