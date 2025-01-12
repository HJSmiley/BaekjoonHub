import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == 1:
        break
    else:
        arr = []

        for i in range(2, n+1):
            while n % i == 0:
                arr.append(i)
                print(i)
                n //= i
        break