s = list(input())

for i in range(len(s)):
    c = s[i]
    if 65 <= ord(c) <= 77 or 97 <= ord(c) <= 109:
        s[i] = chr(ord(c)+13)
    elif 78 <= ord(c) <= 90 or 110 <= ord(c) <= 122:
        s[i] = chr(ord(c)-13)

print(*s, sep='')