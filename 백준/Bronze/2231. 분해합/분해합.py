import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(1, n):
    total = i
    i = str(i)
    for j in range(len(i)):
        total += int(i[j])
    if total == n:
        answer = i
        break

print(answer)