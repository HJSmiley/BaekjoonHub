import sys

input = lambda: sys.stdin.readline().rstrip()

answer = []
n = int(input())

schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x: (x[1], x[0]))

for s, e in schedule:
    if answer and s < answer[-1]:
        continue
    answer.append(e)

print(len(answer))