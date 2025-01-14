import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
answer = 0
d = set()

for _ in range(n):
    txt = input()
    if txt == 'ENTER':
        answer += len(d)
        d = set()
    else:
        d.add(txt)

answer += len(d)

print(answer)