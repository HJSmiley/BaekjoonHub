a = []
b = 0

for _ in range(4):
    a.append(int(input()))
a.sort()

for _ in range(2):
    temp = int(input())
    if temp > b:
        b = temp

print(sum(a[1:])+b)