while True:
    try:
        cntL = cntU = cntN = cntB = 0
        arr = input()
        for c in arr:
            if 97 <= ord(c) <= 122:
                cntL += 1
            elif 65 <= ord(c) <= 90:
                cntU += 1
            elif 48 <= ord(c) <= 57:
                cntN += 1
            elif ord(c) == 32:
                cntB += 1
        print(cntL, cntU, cntN, cntB, end=' ')
        print()
    except EOFError:
        break