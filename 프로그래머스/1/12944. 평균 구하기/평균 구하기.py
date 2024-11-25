def solution(arr):
    answer = 0
    length = len(arr)
    for i in range(length):
        answer += arr[i]
    answer /= length
    return answer