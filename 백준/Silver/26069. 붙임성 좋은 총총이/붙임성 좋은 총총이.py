import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = {'ChongChong'}

for _ in range(n):
    a, b = map(str, input().split())

    if a in s:
        s.add(b)
    if b in s:
        s.add(a)

print(len(s))