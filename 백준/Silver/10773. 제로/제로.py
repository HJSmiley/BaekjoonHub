from collections import deque

q = deque()
total = 0
k = int(input())

for _ in range(k):
    num = int(input())
    if num != 0:
        q.append(num)
    else:
        q.pop()

while q:
    total += q.pop()

print(total)