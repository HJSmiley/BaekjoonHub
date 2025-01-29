import sys
input = lambda: sys.stdin.readline().rstrip()

def exp5(n):
    cnt = 0
    while n > 0:
        cnt += n//5
        n //= 5
    return cnt

def exp2(n):
    cnt = 0
    while n > 0:
        cnt += n//2
        n //= 2
    return cnt

n, m = map(int, input().split())

cnt2 = exp2(n) - exp2(n-m) - exp2(m)
cnt5 = exp5(n) - exp5(n-m) - exp5(m)

print(min(cnt2, cnt5))