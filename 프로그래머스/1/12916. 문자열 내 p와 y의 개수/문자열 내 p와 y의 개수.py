def solution(s):
    pcnt = 0
    ycnt = 0
    for i in range (0, len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pcnt += 1
        elif s[i] == 'y' or s[i] == 'Y':
            ycnt += 1
    if pcnt != ycnt:
        return False
    return True