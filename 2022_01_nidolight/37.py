def solution(n, costs):
    costs.sort(key=lambda x: (x[2]))
    answer = 0

    for c in costs:
        answer+=c[2]

    return answer


print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

