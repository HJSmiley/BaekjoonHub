t = int(input())

for _ in range(t):
    n = int(input())
    s1 = s2 = 0

    for _ in range(n):
        p1, p2 = input().split()
        if p1 != p2:
            if p1 == 'R':
                if p2 == 'P':
                    s2 += 1
                else:
                    s1 += 1
            elif p1 == 'P':
                if p2 == 'R':
                    s1 += 1
                else:
                    s2 += 1
            else:
                if p2 == 'R':
                    s2 += 1
                else:
                    s1 += 1

    if s1 > s2:
        print("Player 1")
    elif s2 > s1:
        print("Player 2")
    else:
        print("TIE")