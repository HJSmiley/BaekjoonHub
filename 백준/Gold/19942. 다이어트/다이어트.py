n = int(input())
mp, mf, ms, mv = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(n)]
min_c = float("inf")
choose = []
answer = []

def recur(idx, p, f, s, v, c):
    global n, min_c, choose, answer

    if c > min_c:
        return

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if c < min_c:
            min_c = c
            answer = choose[:]
        elif c == min_c:
            if choose < answer:
                answer = choose[:]

    if idx == n:
        return

    choose.append(idx + 1)
    recur(idx + 1, p + ingre[idx][0], f + ingre[idx][1], s + ingre[idx][2], v + ingre[idx][3], c + ingre[idx][4])
    choose.pop()

    recur(idx + 1, p, f, s, v, c)

recur(0, 0, 0, 0, 0, 0)

if min_c == float("inf"):
    print(-1)
else:
    print(min_c)
    print(*answer)