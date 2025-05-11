students = [False for _ in range(31)]

for _ in range(28):
    n = int(input())
    students[n] = True

for i in range(1, 31):
    if students[i] == False:
        print(i)