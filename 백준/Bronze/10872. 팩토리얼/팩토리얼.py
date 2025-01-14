n = int(input())
answer = 1

if n == 0:
    print(answer)
else:
    while n != 0:
        answer *= n
        n -= 1
    print(answer)