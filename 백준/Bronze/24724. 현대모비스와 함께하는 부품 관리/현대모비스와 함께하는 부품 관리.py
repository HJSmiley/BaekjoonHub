import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for i in range(1, t + 1):
    print(f"Material Management {i}")
    n = int(input())
    input()
    for _ in range(1, n + 1):
        input()
    print("Classification ---- End!")