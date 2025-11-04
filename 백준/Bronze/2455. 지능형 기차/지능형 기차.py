max = 0
cum = 0

for _ in range(4):
    s, e = map(int, input().split())
    cum -= s
    if cum > max:
        max = cum
    cum += e
    if cum > max:
        max = cum

print(max)