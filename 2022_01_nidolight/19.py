def solution(n, lost, reserve):
    n = set(range(1,n+1))
    lost = set(lost)
    reserve = set(reserve)

    intersection = reserve & lost #교집합

    lost -= intersection
    reserve -= intersection

    #체육복이 없는 친구의 수를 찾자
    for i in lost:
        if i-1 in reserve:
            reserve -= {i-1}
        elif i+1 in reserve:
            reserve -= {i+1}
        else:
            n -= {i}

    return len(n)

(solution(5,[2, 4],[1,3,5]))