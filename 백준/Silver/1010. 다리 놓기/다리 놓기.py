import sys
from math import factorial

input = sys.stdin.readline

def comb(n, k):
    return factorial(n) // (factorial(n-k) * factorial(k))

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(comb(m, n))