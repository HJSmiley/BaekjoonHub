s = input()
holes = ["A", "a", "b", "D", "d", "e", "g", "O", "o", "P", "p", "Q", "q", "R", "@"]
res = 0

for c in s:
    if c in holes:
        res += 1
    elif c == "B":
        res += 2

print(res)