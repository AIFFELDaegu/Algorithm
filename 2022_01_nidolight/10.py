import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        # print(scoville)
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville)+
                                     heapq.heappop(scoville)*2) #(우선 순위, 값)
            answer += 1
        else:
            return -1

    return answer


print(solution([1, 3, 3, 9, 10, 12], 20))

'''
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!

heapq.heappop(minheap)      # pop from minheap
heapq._heappop_max(maxheap) # pop from maxheap
'''