m = int(input())
n = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

tot = 0
min = 10001

for i in range(m, n + 1):
    if is_prime(i):
        tot += i
        if i < min:
            min = i

if tot == 0:
    print(-1)
else:
    print(tot)
    print(min)