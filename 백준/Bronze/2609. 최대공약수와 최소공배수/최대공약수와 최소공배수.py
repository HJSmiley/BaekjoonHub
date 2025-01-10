def GCD(a, b):
    if a%b == 0:
        return b
    return GCD(b, a%b)

def LCM(a, b):
    return a*b//GCD(a,b)

a, b = map(int, input().split())

print(GCD(a, b))
print(LCM(a, b))