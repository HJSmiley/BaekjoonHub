for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())

    h = h2 - h1

    if m2 < m1:
        h -= 1
        m2 += 60
    m = m2 - m1

    if s2 < s1:
        if m != 0:
            m -= 1
            s2 += 60
        else:
            h -= 1
            m += 59
            s2 += 60
    s = s2 - s1

    print(h, m, s)