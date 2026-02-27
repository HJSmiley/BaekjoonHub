n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
white = blue = 0

def solve(x, y, n):
    global white, blue

    color = papers[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if papers[i][j] != color:
                half = n // 2
                solve(x, y, half)
                solve(x, y + half, half)
                solve(x + half, y, half)
                solve(x + half, y + half, half)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

solve(0, 0, n)

print(white)
print(blue)