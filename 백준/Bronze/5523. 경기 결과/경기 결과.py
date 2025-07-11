import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a_score = b_score = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a_score += 1
    elif b > a:
        b_score += 1

print(a_score, b_score)