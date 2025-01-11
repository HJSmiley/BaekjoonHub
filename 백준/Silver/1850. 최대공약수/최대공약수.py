import sys
input = lambda: sys.stdin.readline().rstrip()

def GCD(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

a, b = map(int, input().split())
print('1' * GCD(a, b))