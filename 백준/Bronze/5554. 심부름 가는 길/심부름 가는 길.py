y = 0

for _ in range(4):
    y += int(input())

x = y // 60
y %= 60

print(x, y, sep='\n')