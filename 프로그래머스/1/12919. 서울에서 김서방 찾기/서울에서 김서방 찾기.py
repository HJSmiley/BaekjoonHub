def solution(seoul):
    answer = ''
    for arr in seoul:
        if arr == 'Kim':
            answer = '김서방은 ' + str(seoul.index(arr)) + '에 있다'
    return answer