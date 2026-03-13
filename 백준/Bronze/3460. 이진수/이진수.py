n = int(input())

for _ in range(n):
    t = bin(int(input()))[2:][::-1]
    for i in range(len(t)):
        if t[i] == "1":
            print(i, end=" ")
    print()