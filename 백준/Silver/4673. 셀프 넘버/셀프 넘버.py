n = [i for i in range(1, 10001)]
d = []

for i in range(4):
    for j in range(10**i, 10 ** (i + 1)):
        digit_sum = sum(int(x) for x in str(j))
        d.append(j + digit_sum)

print(*sorted(list((set(n) - set(d)))), sep="\n")