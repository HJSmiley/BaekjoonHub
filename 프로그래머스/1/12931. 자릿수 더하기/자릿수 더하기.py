def solution(n):
    answer = 0
    # n의 자릿수를 구한다 (예 : 3자리)
    # 자릿수 구하는 방법: 1, 10, 100, ... 로 몫이 0이 될 때까지 나누기 -> 0 되기 직전 값
    i = 1
    while (n // i > 0):
        i *= 10
    i //= 10
    # n을 100으로 나누고 몫과 나머지를 구한다 -> 몫을 answer에 더하고 나머지는 이 과정을 반복
    while (i > 0):
        answer += (n // i)
        n %= i
        i //= 10
    return answer