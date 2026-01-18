time = 1500

for _ in range(4):
    time -= int(input())

if time >= 0:
    print("Yes")
else:
    print("No")