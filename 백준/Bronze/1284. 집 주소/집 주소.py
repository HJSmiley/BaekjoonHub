n = input()
w = 1

while int(n) != 0:
    for i in n:
        if int(i) == 1:
            w += 2
        elif int(i) == 0:
            w += 4
        else:
            w += 3
        w += 1
    print(w)

    w = 1
    n = input()