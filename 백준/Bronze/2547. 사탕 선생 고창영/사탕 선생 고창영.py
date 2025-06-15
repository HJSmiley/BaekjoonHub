import sys
input = lambda: sys.stdin.readline()

t = int(input())
enter = input()

for _ in range(t):
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())
    if total % n == 0:
        print('YES')
    else:
        print('NO')
    enter = input()