from collections import deque

def solution(n, costs):
    costs.sort(key=lambda x: (x[2]))
    answer = 0
    visited = deque()

    current = costs.pop(0)
    visited.append(current[0])
    visited.append(current[1])
    answer+=current[2]
    
    while len(visited)<n:
        print(costs)
        print(visited)

        tmp1 = []
        tmp2 = []
        for c in costs: 
            if c[0] == visited[0] or c[1] == visited[0]:
                tmp1=c
                break
        for c in costs: 
            if c[0] == visited[-1] or c[1] == visited[-1]:
                tmp2=c
                break
        if not tmp1:
            for c in costs: 
                if c[0] not in  visited or c[1] not in visited:
                    tmp1=c
                    break
        if not tmp2: 
            for c in costs: 
                if c[0] not in  visited or c[1] not in visited:
                    tmp2=c
                    break

        print(tmp1)
        print(tmp2)
        print()


        if ((tmp1[0] in visited)and (tmp1[1] in visited)):
            costs.remove(tmp1)
            continue
        if ((tmp2[0] in visited)and (tmp2[1] in visited)):
            costs.remove(tmp2)
            continue



        if tmp1[2]<tmp2[2] and (tmp1[0] in visited or tmp1[1] in visited):
            visited.appendleft(tmp1[0] if tmp1[0] not in visited else tmp1[1])
            costs.remove(tmp1)
            answer+=tmp1[2]
        elif (tmp2[0] in visited or tmp2[1] in visited):
            visited.append(tmp2[0] if tmp2[0] not in visited else tmp2[1])
            costs.remove(tmp2)
            answer+=tmp2[2]
        elif (tmp1[0] in visited or tmp1[1] in visited):
            visited.appendleft(tmp1[0] if tmp1[0] not in visited else tmp1[1])
            costs.remove(tmp1)
            answer+=tmp1[2]


    return answer 


print(solution(7, [ [2,3,7],[3,6,13],[3,5,23],[5,6,25],[0,1,29],[1,5,34],[1,2,35],[4,5,53],[0,4,75] ] ))

# 크루스칼 알고리즘: https://whwl.tistory.com/m/245
# testcase: https://programmers.co.kr/questions/17069