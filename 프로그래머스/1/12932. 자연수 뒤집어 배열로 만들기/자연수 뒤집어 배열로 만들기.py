def solution(n):
    answer = []
    n = str(n)
    length = len(n)
    for i in range(length):
        answer.append(int(n[length-i-1]))
    return answer