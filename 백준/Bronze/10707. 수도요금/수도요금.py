a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

if p <= c:
    print(min(a * p, b))
else:
    print(min(a * p, b + (p - c) * d))