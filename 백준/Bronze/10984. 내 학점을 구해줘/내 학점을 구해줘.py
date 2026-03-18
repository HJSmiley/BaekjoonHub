t = int(input())

for _ in range(t):
    tot_c = 0
    tot_g = 0

    n = int(input())
    for _ in range(n):
        c, g = map(float, input().split())
        tot_c += c
        tot_g += c * g

    print(int(tot_c), "{:.1f}".format(tot_g / tot_c))