import sys
input = lambda : sys.stdin.readline().rstrip()

def cycle(x):
    return (x % 10) * 10 + ((x // 10) + (x % 10)) % 10

n = int(input())
tmp = n

n = cycle(n)
cnt = 1

while n != tmp:
    n = cycle(n)
    cnt += 1

print(cnt)