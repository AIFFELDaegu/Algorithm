#어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
#나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

def solution(citations):
    answer = 0
    citations.sort()
    length=len(citations)
    for i in range(length):
        h = length-i
        if h <= citations[i]:
            answer = h
            break
    return answer


# print(solution([3, 0, 6, 1, 5]))
print(solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20]))
