arr = input()
d = []

for i in range(len(arr)):
    d.append(arr[i:])

for j in sorted(d):
    print(j)