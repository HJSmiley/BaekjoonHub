import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

def GCD(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

n = int(input())

for _ in range(n):
    total = 0
    arr = list(map(int, input().split()))
    for i in combinations(arr[1:], 2):
        total += GCD(i[0], i[1])
    print(total)