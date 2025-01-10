word = input()
ans = [-1] * 26

for i in range(len(word)):
    c = word[i]
    if ans[ord(c)-97] != -1:
        continue
    ans[ord(c)-97] = i

print(*ans)