def GCD(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def LCM(a, b):
    return a * b // GCD(a, b)

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(LCM(a, b))