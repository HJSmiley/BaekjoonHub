import sys

input = lambda: sys.stdin.readline().rstrip()

m = int(input())
s = set()

for _ in range(m):
    op = input().split()
    command = op[0]
    if command == "add":
        s.add(int(op[1]))
    elif command == "remove":
        s.discard(int(op[1]))
    elif command == "check":
        if int(op[1]) in s:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if int(op[1]) in s:
            s.remove(int(op[1]))
        else:
            s.add(int(op[1]))
    elif command == "all":
        s = set(range(1, 21))
    elif command == "empty":
        s.clear()