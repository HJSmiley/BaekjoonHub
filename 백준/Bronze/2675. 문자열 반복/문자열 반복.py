t = int(input())

for _ in range(t):
    r, s = map(str, input().split())
    r = int(r)
    for c in s:
        print(c*r, end='')
    print()