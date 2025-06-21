odd = []

for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        odd.append(num)

if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))