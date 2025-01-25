maxN = int(input())
cnt = 1
maxCnt = cnt

while True:
    try:
        n = int(input())
        cnt += 1
        if n > maxN:
            maxN = n
            maxCnt = cnt
    except EOFError:
        break

print(maxN)
print(maxCnt)