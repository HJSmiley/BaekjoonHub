# def solution(number, k):
#     # 내림차순 정렬 -> 앞자리 k개 제거
#     number = sorted(str(number), reverse=True)[:-k]
#     return number

# def solution(number, k):
#     answer = ''
#     cnt = 0
#     number = str(number)
#     n = len(number)
    
#     for i in range(1, n-k):
#         if int(number[i-1:i-1+k]) < int(number[i:i+k]):
#             print(i, number[i:i+k])
#             answer += number[i+1]
#             cnt += 1
#         if cnt == k:
#             answer += number[i+1:]
#             print(i)
#             return answer
    
#     return answer

def solution(number, k):
    s = []
    
    for num in number:
        while s and k > 0 and s[-1] < num:
            s.pop()
            k -= 1
        s.append(num)
        
    if k > 0:
        s = s[:-k]
        
    return "".join(s)