a, b = map(int, input().split())
m = int(input())
n = input().split()

chars = '0123456789ABCDEFGHIJKLMNOPQRST'
mod_dict = {i: chars[i] for i in range(30)}

for i, c in enumerate(n):
    n[i] = mod_dict[int(c)]

n = int(''.join(n), a)
answer = []

while n:
    answer.append(n % b)
    n //= b

print(*answer[::-1])