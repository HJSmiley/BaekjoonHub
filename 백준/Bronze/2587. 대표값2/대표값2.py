import sys

arr = list(map(int, sys.stdin.readlines()))

print(int(sum(arr) / len(arr)))
print(sorted(arr)[int(len(arr)/2)])