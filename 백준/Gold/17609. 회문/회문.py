t = int(input())

def is_palindrome(s):
    sp = 0
    ep = len(s) - 1

    while sp <= ep:
        if s[sp] != s[ep]:
            l_skip = s[sp + 1 : ep + 1]
            r_skip = s[sp:ep]
            
            if l_skip == l_skip[::-1] or r_skip == r_skip[::-1]:
                return 1
            else:
                return 2

        sp += 1
        ep -= 1

    return 0

for _ in range(t):
    print(is_palindrome(input()))