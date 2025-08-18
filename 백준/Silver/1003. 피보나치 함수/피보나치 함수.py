d0 = [0 for _ in range(41)]
d1 = [0 for _ in range(41)]
d0[0] = 1; d0[1] = 0
d1[0] = 0; d1[1] = 1

for i in range(2, 41):
    d0[i] = d0[i-1] + d0[i-2]
    d1[i] = d1[i-1] + d1[i-2]

t = int(input())

for _ in range(t):
    n = int(input())
    print(d0[n], d1[n])