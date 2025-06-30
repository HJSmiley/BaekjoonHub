import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
lst = [int(input()) for _ in range(n)]
res = 1

for i in lst:
    res += i-1

print(res)