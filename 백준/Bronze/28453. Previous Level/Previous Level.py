n = int(input())
levels = map(int, input().split())
for level in levels:
    sect = (
        1
        if level == 300
        else 2 if 275 <= level < 300 else 3 if 250 <= level < 275 else 4
    )
    print(sect, end=" ")
