h, w = map(int, input().split())
joi = [list(input()) for _ in range(h)]

for j in range(h):
    cur_cl = -1
    for i in range(w):
        if joi[j][i] == "c":
            print(0, end=" ")
            cur_cl = 0
        else:
            if cur_cl == -1:
                print(-1, end=" ")
            else:
                cur_cl += 1
                print(cur_cl, end=" ")
    print()