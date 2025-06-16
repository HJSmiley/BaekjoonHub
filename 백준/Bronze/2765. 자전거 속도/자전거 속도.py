i = 0

while True:
    try:
        i += 1

        d, c, t = map(float, input().split())
        c = int(c)
        if c == 0:
            continue

        distance = d / 12 / 5280 * 3.1415927 * c
        mph = distance / (t / 60 / 60)

        print(f"Trip #{i}: {distance:.2f} {mph:.2f}")
        
    except EOFError:
        break