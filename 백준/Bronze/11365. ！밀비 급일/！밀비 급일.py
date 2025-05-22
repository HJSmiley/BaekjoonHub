while True:
    s = input()
    if s == "END":
        break
    print(*list(reversed(list(s))), sep='')