t = int(input())

for _ in range(t):
    res = 0
    s = set(input())

    for c in range(65, 91):
        if chr(c) not in s:
            res += c

    print(res)