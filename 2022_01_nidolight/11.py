import heapq

def solution(jobs):
    answer = 0
    start = 0 
    tmpJ = []
    newJ = []

    for j in jobs:
        tmpJ.append([j[1], j[0]]) 
    heapq.heapify(tmpJ)# j[0]기

    while tmpJ:
        k = heapq.heappop(tmpJ)
        newJ.append([k[1], k[0]])
    print(newJ)

    while len(newJ) != 0:
        for i in range(len(newJ)):
            if newJ[i][0] <= start:
                start += newJ[i][1]
                answer += start - newJ[i][0]
                newJ.pop(i)
                break
            if i == len(newJ) - 1:
                start += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))

'''
SJF알고리즘(최소작업우선 알고리즘)
- 요청시간 순서대로 정렬을하고
- 요청시간이 같다면 처리시간이 작은순서대로 정렬
'''