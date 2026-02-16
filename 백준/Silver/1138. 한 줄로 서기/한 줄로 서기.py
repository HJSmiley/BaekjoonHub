import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lst = zip([i for i in range(1, n + 1)], list(map(int, input().split())))
answer = [0] * n

for num, left in lst:
    step = 0
    for j in range(n):
        if answer[j] == 0:
            if step == left:
                answer[j] = num
                break
            step += 1

print(*answer)