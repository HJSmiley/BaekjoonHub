import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
q = deque()
ans = []

for i in range(n):
    q.append(str(i+1))

while q:
    for i in range(k):
        q.append(q.popleft())
    ans.append(q.pop())

print('<' + ', '.join(ans) + '>')