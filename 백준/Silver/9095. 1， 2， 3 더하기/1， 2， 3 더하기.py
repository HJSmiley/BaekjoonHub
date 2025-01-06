t = int(input())

d = [0] * 13
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(1, 8):
    d[i+3] = d[i+2] + d[i+1] + d[i]

for j in range(t):
    n = int(input())
    print(d[n])