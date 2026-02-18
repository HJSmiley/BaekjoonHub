import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
s = input()

answer = 0
count = 0
idx = 0

while idx < m - 1:
    if s[idx : idx + 3] == "IOI":
        count += 1

        if count == n:
            answer += 1
            count -= 1

        idx += 2
    else:
        count = 0
        idx += 1

print(answer)