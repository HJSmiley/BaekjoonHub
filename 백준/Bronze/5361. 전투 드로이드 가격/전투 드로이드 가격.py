t = int(input())

for _ in range(t):
    a, b, c, d, e = map(int, input().split())
    print(f"${350.34*a + 230.90*b + 190.55*c + 125.30*d + 180.90*e:.2f}")