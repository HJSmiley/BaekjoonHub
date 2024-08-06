def solution(n, k):
    answer = 12000 * n + 2000 * k
    if (n >= 10):
        answer -= 2000 * (n // 10)
    return answer