import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

doc = input()
word = input()
n = len(doc)
m = len(word)
answer = []

for i in range(n):
    sp = i
    count = 0

    while sp < n:
        if doc[sp : sp + m] == word:
            count += 1
            sp += m
        else:
            sp += 1

    heapq.heappush(answer, -count)

print(-heapq.heappop(answer))