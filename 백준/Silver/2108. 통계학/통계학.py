import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

print(round(sum(arr)/n))

arr = sorted(arr)
print(arr[int(len(arr)//2)])

d = dict()
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

key = [k for k, v in d.items() if max(d.values()) == v]
if len(key) != 1:
    print(key[1])
else:
    print(key[0])

print(max(arr)-min(arr))