n = int(input())

d = [0] * (n + 3)
d[1] = 1
d[2] = 3

for i in range(1, n+1):
    d[i+2] = d[i+1] + 2*d[i]

print(d[n]%10007)