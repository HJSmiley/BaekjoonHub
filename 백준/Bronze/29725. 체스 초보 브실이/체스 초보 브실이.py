ws = 0
bs = 0

for _ in range(8):
    lst = input()
    for i in range(8):
        p = lst[i]
        if p == '.' or p == 'K' or p == 'k':
            continue
        elif p == 'P':
            ws += 1
        elif p == 'p':
            bs += 1
        elif p == 'N' or p == 'B':
            ws += 3
        elif p == 'n' or p == 'b':
            bs += 3
        elif p == 'R':
            ws += 5
        elif p == 'r':
            bs += 5
        elif p == 'Q':
            ws += 9
        elif p == 'q':
            bs += 9

print(ws-bs)