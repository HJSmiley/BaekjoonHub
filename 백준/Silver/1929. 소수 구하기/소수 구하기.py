m, n = map(int, input().split())
a = min(m, n)
b = max(m, n)
d = [True] * (b + 1)
d[0] = False
d[1] = False

for i in range(2, int(b**0.5)+1):
    if d[i] == False:
        continue
    for j in range(2*i, b+1, i):
        d[j] = False

for k in range(a, b+1):
    if d[k] == True:
        print(k)