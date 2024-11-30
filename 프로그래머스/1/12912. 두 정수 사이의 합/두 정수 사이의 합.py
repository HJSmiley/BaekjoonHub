def solution(a, b):
    answer = 0
    if (a > b):
        i = b
        while (a >= i >= b):
            answer += i
            i += 1
    elif (a < b):
        i = a
        while (a <= i <= b):
            answer += i
            i += 1
    else:
        return a
    return answer