from itertools import permutations

def solution(k, dungeons):
    answer = []
    p = list(permutations(range(len(dungeons))))

    for i in range(len(p)):
        nums = p[i]
        cur = k
        tmp = 0

        for j in nums:
            l, c = dungeons[j]
            
            if cur >= l:
                cur -= c
                tmp += 1
            else:
                break
        
        answer.append(tmp)

    return max(answer)