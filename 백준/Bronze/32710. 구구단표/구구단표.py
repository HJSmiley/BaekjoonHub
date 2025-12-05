n = int(input())

a = set(range(2, 10))
b = set(range(1, 10))
c = {i * j for i in range(2, 10) for j in range(1, 10)}
s = a | b | c

print(1 if n in s else 0)