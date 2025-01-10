word = list(map(str, input()))
answer = [0] * 26

for c in word:
    answer[ord(c)-97] += 1

for i in answer:
    print(i, end=' ')