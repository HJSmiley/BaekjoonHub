n = int(input())
score = [0 for _ in range(n)]

for i in range(n):
    a, d, g = map(int, input().split())
    score[i] = a * (d + g)
    if a == (d + g):
        score[i] *= 2

print(max(score))
