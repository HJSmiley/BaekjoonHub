import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] >= K:
        return 0

    while len(scoville) > 1:
        l1 = heapq.heappop(scoville)
        l2 = heapq.heappop(scoville)
        heapq.heappush(scoville, l1 + l2 * 2)
        answer += 1
        
        if scoville[0] >= K:
            return answer
        
    return -1