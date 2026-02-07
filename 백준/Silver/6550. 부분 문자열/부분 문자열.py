while True:
    try:
        s, t = input().split()
        answer = []
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    answer.append(s[i])
                    t = t[j + 1 :]
                    break
        if ''.join(answer) == s:
            print("Yes")
        else:
            print("No")

    except EOFError:
        break