word = input()
result = []

for c in word:
    if c.isupper():
        result.append(c.lower())
    else:
        result.append(c.upper())

print(*result, sep='')