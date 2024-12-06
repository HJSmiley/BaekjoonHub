# 뒤집어서 배치하라는 줄 알았네;;
# def solution(n):
#     answer = int(''.join(reversed(str(n))))
#     return answer

# 자릿수를 큰 것부터 작은 순까지 정렬
# sorted() 함수는 문자열 기준으로 정렬할 때 정상적으로 동작
def solution(n):
    # 숫자->문자열->리스트로 변환 후 내림차순 정렬
    # 이후 각 원소를 공백으로 join한 뒤 숫자형으로 변환
    answer = int(''.join(sorted(list(str(n)), reverse=True)))
    return answer