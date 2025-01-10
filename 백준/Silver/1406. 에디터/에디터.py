import sys
input = lambda: sys.stdin.readline().rstrip()

word1 = list(input())
word2 = []

m = int(input())

for _ in range(m):
    o = input().split()

    if o[0] == 'L' and word1:
        word2.append(word1.pop())
    elif o[0] == 'D' and word2:
        word1.append(word2.pop())
    elif o[0] == 'B' and word1:
        word1.pop()
    elif o[0] == 'P':
        word1.append(o[1])

answer = word1 + word2[::-1]
print(*answer, sep='')