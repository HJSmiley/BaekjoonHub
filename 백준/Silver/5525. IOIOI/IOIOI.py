import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
s = input()

pn = "I" + "OI" * n
answer = 0
idx = 0

for c in s:
    if c == "I" and s[idx : idx + 2 * n + 1] == pn:
        answer += 1
        if idx + 2 * n + 1 == m:
            break
    idx += 1

print(answer)