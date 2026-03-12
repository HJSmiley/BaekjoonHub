n = input()
dt = {i: 0 for i in range(10)}

for c in n:
    c = int(c)
    if c == 6 or c == 9:
        dt[6] += 1
    else:
        dt[c] += 1

dt[6] = (dt[6] + 1) // 2

print(max(dt.values()))