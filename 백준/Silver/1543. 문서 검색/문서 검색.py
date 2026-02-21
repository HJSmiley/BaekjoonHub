doc = input()
word = input()
n = len(doc)
m = len(word)

count = 0
idx = 0

while idx <= n - m:
    if doc[idx : idx + m] == word:
        count += 1
        idx += m
    else:
        idx += 1

print(count)