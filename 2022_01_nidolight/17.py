def solution(answers):
    answer = {1:0,2:0,3:0}

    person = [[],
              [1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(1,4):
        for a in answers:
            poped = person[i].pop(0)
            person[i].append(poped)
            if a == poped:
                answer[i] += 1

    max_score = 0
    for a in answer:
        if max_score <= answer[a]:
            max_score = answer[a]
            
    ans = [a for a in answer if answer[a] == max_score]
    ans.sort()

    return ans

print(solution([3,3,2,4,2,1]))

"""
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5 ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5 ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ...
"""
