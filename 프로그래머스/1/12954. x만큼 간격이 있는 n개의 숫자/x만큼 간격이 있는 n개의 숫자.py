def solution(x, n):
    answer = []
    # x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트
    for i in range(n):
        answer.append((i+1)*x)
    return answer