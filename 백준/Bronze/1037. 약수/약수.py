import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
arr = list(map(int, input().split()))

if t != 1:
    arr = sorted(arr)
    n = arr[0] * arr[-1]
else:
    n = arr[0] ** 2

print(n)