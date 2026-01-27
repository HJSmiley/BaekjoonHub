from collections import deque

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))
dq = deque()
ans = []

for i in range(n):
    if A[i] == 0:
        dq.append(B[i])

for x in C:
    dq.appendleft(x)
    ans.append(dq.pop())

print(*ans)