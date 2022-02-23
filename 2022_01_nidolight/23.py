def solution(triangle):
    answer = triangle[0]

    answer = recursive(triangle[1:],answer)

    return max(answer)

def recursive(triangle, answer):
    tmp = []
    
    # print("ans: {}\n in: {}\n".format(answer,triangle))

    if not triangle:#비어있다면 종료
        return answer

    for i, n in enumerate(triangle[0]):
        if i == 0:
            tmp.append(answer[0]+n)
        elif i == len(triangle[0])-1:
            tmp.append(answer[-1]+n)
        else:
            tmp.append(max(answer[i-1]+n,answer[i]+n))

    return recursive(triangle[1:],tmp)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))