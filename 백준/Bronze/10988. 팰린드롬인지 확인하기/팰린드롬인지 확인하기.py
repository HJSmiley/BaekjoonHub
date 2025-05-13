word = input()
lst = []
flag = True

if len(word) % 2 == 0:
    for i in range(len(word)//2):
        lst.append(word[i])
    for j in range(len(word)//2, len(word)):
        if word[j] != lst.pop():
            flag = False
            break
    if flag:
        print(1)
    else:
        print(0)
else:
    for i in range(len(word)//2):
        lst.append(word[i])
    for j in range(len(word)//2+1, len(word)):
        if word[j] != lst.pop():
            flag = False
            break
    if flag:
        print(1)
    else:
        print(0)