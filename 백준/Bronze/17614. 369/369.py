n = int(input())
count = 0

for i in range(3, n + 1):
    s = str(i)
    count += s.count("3") + s.count("6") + s.count("9")

print(count)