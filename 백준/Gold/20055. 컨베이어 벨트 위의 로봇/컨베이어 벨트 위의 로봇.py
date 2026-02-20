import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
belt = deque(map(int, input().split()))

robots = deque([False] * n)
zero_count = belt.count(0)
stage = 0

while zero_count < k:
    stage += 1

    belt.rotate(1)
    robots.rotate(1)
    robots[n - 1] = False

    for i in range(n - 2, -1, -1):
        if robots[i] and not robots[i + 1] and belt[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            belt[i + 1] -= 1

            if belt[i + 1] == 0:
                zero_count += 1

    robots[n - 1] = False

    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            zero_count += 1

print(stage)