n = int(input())
an = list(map(int, input().split()))
answer = [-1] * n
s = []

for i, a in enumerate(an):
    while s and a > an[s[-1]]:
        answer[s.pop()] = a
    s.append(i)

print(*answer)