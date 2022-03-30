from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 1
    total_weight = 0

    while people:
        total_weight = people.pop()
        for i, p in enumerate(people):
            if total_weight+p <= limit:
                total_weight+=p
            else:
                answer+=1
                total_weight=0
                for _ in range(i):
                    people.popleft()
                break
            
    return answer


print(solution([70, 50, 80, 50,10],100))